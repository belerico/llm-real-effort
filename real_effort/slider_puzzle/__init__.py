import json
import time

from otree import settings
from otree.api import *

from config import get_game_config, update_payoff, payoff_summary, export_puzzle_rows

from . import slider_puzzle
from .image_utils import encode_image

doc = """
Sliding tile puzzle (single player). Arrange numbered tiles in order by
sliding them into the empty space.
"""


class C(BaseConstants):
    NAME_IN_URL = "slider_puzzle"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    INSTRUCTION_TEMPLATE = __name__ + "/instructions.html"


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    session = subsession.session
    game_cfg = get_game_config("slider_puzzle")
    defaults = dict(
        retry_delay=0.0,
        puzzle_delay=1.0,
        attempts_per_puzzle=1,
        max_iterations=1,
        size=3,
        num_shuffles=25,
        timeout=60,
        puzzle_timeout=0,
        incentive=False,
        incentive_text="You will earn a bonus of $0.10 for each correct answer.",
        bonus_per_correct=0.2,
    )
    # Merge into shared params — in a multi-app session oTree runs every app's
    # creating_session, so don't wipe params set by the other games.
    session.params = session.params if session.params is not None else {}
    for param in defaults:
        session.params[param] = game_cfg.get(
            param, session.config.get(param, defaults[param])
        )
    reps = game_cfg.get("repetitions", session.config.get("repetitions"))
    if reps is not None:
        session.params["max_iterations"] = int(reps)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    iteration = models.IntegerField(initial=0)
    num_trials = models.IntegerField(initial=0)
    num_correct = models.IntegerField(initial=0)
    num_failed = models.IntegerField(initial=0)


class Puzzle(ExtraModel):
    player = models.Link(Player)
    iteration = models.IntegerField(initial=0)
    attempts = models.IntegerField(initial=0)
    timestamp = models.FloatField(initial=0)
    text = models.LongStringField()           # initial board state JSON
    current_state = models.LongStringField()   # current board state JSON
    solution = models.LongStringField()        # optimal move sequence
    response = models.LongStringField()        # actual moves made (space-separated)
    response_timestamp = models.FloatField()
    is_correct = models.BooleanField()


# ── Puzzle helpers ────────────────────────────────────────────────────────


def gen_puzzle(player: Player) -> Puzzle:
    params = player.session.params
    fields = slider_puzzle.generate_puzzle_fields(
        size=params["size"],
        num_shuffles=params["num_shuffles"],
    )
    player.iteration += 1
    return Puzzle.create(
        player=player,
        iteration=player.iteration,
        timestamp=time.time(),
        current_state=fields["text"],  # starts same as initial
        **fields,
    )


def get_cur_puzzle(player: Player):
    puzzles = Puzzle.filter(player=player, iteration=player.iteration)
    if puzzles:
        [puzzle] = puzzles
        return puzzle


def enc_puzzle(puzzle: Puzzle):
    state = json.loads(puzzle.current_state)
    size = int(len(state) ** 0.5)
    image = slider_puzzle.render_board_image(state, size)
    return dict(
        image=encode_image(image),
        state=state,
        size=size,
    )


def get_progress(player: Player):
    update_payoff(player)
    return dict(
        num_trials=player.num_trials,
        num_correct=player.num_correct,
        num_incorrect=player.num_failed,
        iteration=player.iteration,
    )


def custom_export(players):
    """One row per puzzle attempt — appears on the admin Data page."""
    yield from export_puzzle_rows(players, Puzzle, extra_fields=("current_state",))


# ── Live method ───────────────────────────────────────────────────────────


def play_game(player: Player, msg: dict):
    session = player.session
    my_id = player.id_in_group
    params = session.params
    now = time.time()
    current = get_cur_puzzle(player)
    msg_type = msg["type"]

    # Auto-fail a stale puzzle if its per-puzzle timeout was exceeded — a safety
    # net for non-'timeout' messages. Explicit 'timeout' messages are handled by
    # the timeout branch below, which needs current.response to still be None.
    puzzle_timeout = params.get("puzzle_timeout", 0)
    if (
        puzzle_timeout > 0
        and current is not None
        and current.response is None
        and msg_type != "timeout"
    ):
        if now - current.timestamp >= puzzle_timeout:
            current.response = current.response or ""
            current.is_correct = False
            current.response_timestamp = now
            player.num_failed += 1
            player.num_trials += 1

    if msg_type == "load":
        prog = get_progress(player)
        if current:
            return {my_id: dict(type="status", progress=prog, puzzle=enc_puzzle(current))}
        else:
            return {my_id: dict(type="status", progress=prog)}

    if msg_type == "cheat" and settings.DEBUG:
        return {my_id: dict(type="solution", solution=current.solution)}

    if msg_type == "timeout":
        if current is None or current.is_correct is not None:
            return {my_id: dict(type="status", progress=get_progress(player))}
        current.response = current.response or ""
        current.is_correct = False
        current.response_timestamp = now
        player.num_failed += 1
        player.num_trials += 1
        return {
            my_id: dict(
                type="feedback",
                is_correct=False,
                retries_left=0,
                progress=get_progress(player),
                timed_out=True,
            )
        }

    if msg_type == "next":
        if current is not None:
            if current.is_correct is None:
                raise RuntimeError("trying to skip over unsolved puzzle")
            if now < current.timestamp + params["puzzle_delay"]:
                raise RuntimeError("retrying too fast")
            if current.iteration >= params["max_iterations"]:
                return {
                    my_id: dict(
                        type="status",
                        progress=get_progress(player),
                        iterations_left=0,
                    )
                }
        else:
            if player.iteration >= params["max_iterations"]:
                return {
                    my_id: dict(
                        type="status",
                        progress=get_progress(player),
                        iterations_left=0,
                    )
                }
        puzz = gen_puzzle(player)
        prog = get_progress(player)
        return {my_id: dict(type="puzzle", puzzle=enc_puzzle(puzz), progress=prog)}

    if msg_type == "move":
        # Interactive tile move
        if current is None or current.is_correct is not None:
            return {my_id: dict(type="status", progress=get_progress(player))}

        tile = msg.get("tile")
        if tile is None:
            raise ValueError("No tile specified")
        tile = int(tile)

        state = json.loads(current.current_state)
        size = params["size"]

        if not slider_puzzle.apply_move(state, tile, size):
            return {my_id: dict(type="invalid_move", progress=get_progress(player))}

        # Update state
        current.current_state = json.dumps(state)
        current.attempts += 1
        current.response = (
            (current.response + " " + str(tile)) if current.response else str(tile)
        )
        current.response_timestamp = now

        # Check if solved
        if slider_puzzle.is_solved(state, size):
            current.is_correct = True
            player.num_correct += 1
            player.num_trials += 1
            prog = get_progress(player)
            return {
                my_id: dict(
                    type="solved",
                    puzzle=enc_puzzle(current),
                    progress=prog,
                )
            }

        # Return updated state
        return {
            my_id: dict(
                type="moved",
                puzzle=enc_puzzle(current),
                progress=get_progress(player),
            )
        }

    if msg_type == "answer":
        # Text-based answer (move sequence) for LLM compatibility
        if current is None:
            raise RuntimeError("trying to answer no puzzle")

        if current.is_correct is not None:
            raise RuntimeError("puzzle already resolved")

        answer = msg.get("answer", "")
        if answer == "" or answer is None:
            raise ValueError("Answer is empty")

        current.response = answer
        current.is_correct = slider_puzzle.is_correct(answer, current)
        current.response_timestamp = now
        current.attempts += 1

        if current.is_correct:
            # Apply the moves to update current_state
            state = json.loads(current.text)
            size = params["size"]
            for tile in (int(m) for m in answer.strip().split()):
                slider_puzzle.apply_move(state, tile, size)
            current.current_state = json.dumps(state)
            player.num_correct += 1
        else:
            player.num_failed += 1
        player.num_trials += 1

        prog = get_progress(player)
        return {
            my_id: dict(
                type="feedback",
                is_correct=current.is_correct,
                retries_left=0,
                progress=prog,
            )
        }

    raise RuntimeError("unrecognized message from client")


# PAGES


class Game(Page):
    @staticmethod
    def get_timeout_seconds(player: Player):
        return player.session.params.get("timeout", 60)

    live_method = play_game

    @staticmethod
    def js_vars(player: Player):
        return dict(params=player.session.params)

    @staticmethod
    def vars_for_template(player: Player):
        params = player.session.params
        return dict(
            DEBUG=settings.DEBUG,
            input_type=slider_puzzle.INPUT_TYPE,
            placeholder=slider_puzzle.INPUT_HINT,
            incentive_text=params["incentive_text"] if params["incentive"] else "",
            size=params["size"],
        )


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return payoff_summary(player)


class End(Page):
    @staticmethod
    def is_displayed(player: Player):
        max_iter = player.session.params.get("max_iterations", 1)
        return player.iteration >= max_iter

    @staticmethod
    def vars_for_template(player: Player):
        return dict(message="Thank you. You have completed all repetitions.")


page_sequence = [Game, Results, End]

from pathlib import Path

import yaml

_CONFIG_PATH = Path(__file__).resolve().parent / "benchmark_config.yaml"


def load_benchmark_config(config_path=None):
    """Load full YAML config. Returns {} if file doesn't exist."""
    path = Path(config_path) if config_path else _CONFIG_PATH
    if not path.exists():
        return {}
    with open(path) as f:
        return yaml.safe_load(f) or {}


def get_game_config(game_name, config_path=None):
    """Get per-game config dict from YAML.

    Merges global ``game_defaults`` with per-game overrides (per-game wins).
    Returns {} if neither section exists.
    """
    config = load_benchmark_config(config_path)
    defaults = config.get("game_defaults", {}) or {}
    games = config.get("games", {}) or {}
    per_game = games.get(game_name, {}) or {}
    return {**defaults, **per_game}


def update_payoff(player):
    """Recompute ``player.payoff`` from ``num_correct``.

    Pays ``bonus_per_correct`` (in points; converted to real currency by
    oTree via ``real_world_currency_per_point``) for every correct answer
    when ``incentive`` is exactly ``True``. For ``False`` or
    ``"explicit_none"``, payoff is 0. Mirrors the gating used in
    run_benchmarks.py to keep human/LLM treatments aligned.
    """
    params = getattr(player.session, "params", {}) or {}
    if params.get("incentive") is True:
        bonus = float(params.get("bonus_per_correct", 1.0))
        player.payoff = player.num_correct * bonus
    else:
        player.payoff = 0


def payoff_summary(player):
    """End-of-game payout figures for the Results template.

    Recomputes the payoff so it reflects the final ``num_correct``, then
    expresses the bonus and grand total in real-world currency. ``bonus``
    and ``total_pay`` are oTree currency objects; ``total_pay`` already
    includes the session participation fee.
    """
    update_payoff(player)
    session = player.session
    return dict(
        num_correct=player.num_correct,
        num_trials=player.num_trials,
        incentive=session.params.get("incentive") is True,
        bonus=player.payoff.to_real_world_currency(session),
        total_pay=player.participant.payoff_plus_participation_fee(),
    )


def export_puzzle_rows(players, puzzle_model, extra_fields=()):
    """Yield CSV rows (header first) for an app's per-puzzle ExtraModel.

    Used by each app's ``custom_export`` so the puzzle-level data — one row
    per puzzle attempt — is downloadable from the oTree admin Data page,
    matching the grain of the LLM benchmark's ``puzzles`` table.

    ``puzzle_model`` — the app's Puzzle/Question ExtraModel class.
    ``extra_fields`` — extra puzzle attributes to append (e.g. 'current_state').
    """
    header = [
        "session_code", "participant_code", "participant_label", "incentive",
        "num_correct", "num_failed", "num_trials", "payoff",
        "iteration", "attempts", "text", "solution", "response",
        "is_correct", "timestamp", "response_timestamp", "response_time",
    ]
    yield header + list(extra_fields)
    for p in players:
        participant = p.participant
        session = p.session
        params = getattr(session, "params", None) or {}
        for puz in puzzle_model.filter(player=p):
            ts = puz.timestamp or 0
            rts = puz.response_timestamp or 0
            response_time = round(rts - ts, 3) if (ts and rts) else None
            row = [
                session.code, participant.code, participant.label,
                params.get("incentive"),
                p.num_correct, p.num_failed, p.num_trials, p.payoff,
                puz.iteration, puz.attempts, puz.text, puz.solution, puz.response,
                puz.is_correct, puz.timestamp, puz.response_timestamp, response_time,
            ]
            row += [getattr(puz, f, None) for f in extra_fields]
            yield row

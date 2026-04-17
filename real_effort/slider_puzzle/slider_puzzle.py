"""Sliding tile puzzle generation, validation, and image rendering.

Board is a flat list of length size*size, where 0 represents the empty space.
Tiles are numbered 1..size*size-1. Solved state: [1, 2, ..., N, 0].
"""

import json
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

TEXT_FONT = Path(__file__).parent / "assets" / "FreeSerifBold.otf"

INPUT_TYPE = "text"
INPUT_HINT = "enter tile moves separated by spaces (e.g. 5 2 3)"

# Tile rendering constants
TILE_SIZE = 80
TILE_GAP = 4
TILE_COLOR = (59, 130, 246)       # blue
TILE_TEXT_COLOR = (255, 255, 255)  # white
EMPTY_COLOR = (209, 213, 219)     # light gray
BORDER_COLOR = (31, 41, 55)       # dark gray
FONT_SIZE = 32


def _solved_board(size: int) -> list[int]:
    """Return the solved state: [1, 2, ..., size*size-1, 0]."""
    return list(range(1, size * size)) + [0]


def _find_empty(board: list[int], size: int) -> int:
    """Return the index of the empty space (0)."""
    return board.index(0)


def _neighbors(idx: int, size: int) -> list[int]:
    """Return indices of cells adjacent to idx (up/down/left/right)."""
    r, c = divmod(idx, size)
    result = []
    if r > 0:
        result.append((r - 1) * size + c)
    if r < size - 1:
        result.append((r + 1) * size + c)
    if c > 0:
        result.append(r * size + c - 1)
    if c < size - 1:
        result.append(r * size + c + 1)
    return result


def get_movable_tiles(board: list[int], size: int) -> list[int]:
    """Return tile numbers that can be moved (adjacent to empty space)."""
    empty = _find_empty(board, size)
    return [board[n] for n in _neighbors(empty, size)]


def apply_move(board: list[int], tile: int, size: int) -> bool:
    """Move a tile into the empty space. Returns True if valid, False otherwise."""
    empty = _find_empty(board, size)
    try:
        tile_idx = board.index(tile)
    except ValueError:
        return False
    if tile_idx not in _neighbors(empty, size):
        return False
    board[empty], board[tile_idx] = board[tile_idx], board[empty]
    return True


def is_solved(board: list[int], size: int) -> bool:
    """Check if the board is in the solved state."""
    return board == _solved_board(size)


def generate_puzzle_fields(size: int = 3, num_shuffles: int = 25) -> dict:
    """Generate a solvable shuffled puzzle by making random moves from solved state.

    Returns dict with 'text' (initial state JSON) and 'solution' (move sequence).
    """
    board = _solved_board(size)
    moves = []
    last_tile = None

    for _ in range(num_shuffles):
        movable = get_movable_tiles(board, size)
        # Avoid immediately undoing the last move
        if last_tile is not None and last_tile in movable:
            candidates = [t for t in movable if t != last_tile]
            if candidates:
                movable = candidates
        tile = random.choice(movable)
        apply_move(board, tile, size)
        moves.append(tile)
        last_tile = tile

    # Solution: reverse the shuffle moves
    solution = " ".join(str(t) for t in reversed(moves))

    return dict(text=json.dumps(board), solution=solution)


def is_correct(response: str, puzzle) -> bool:
    """Validate a move-sequence answer against the puzzle's initial state."""
    board = json.loads(puzzle.text)
    size = int(len(board) ** 0.5)
    try:
        moves = [int(m) for m in response.strip().split()]
    except (ValueError, AttributeError):
        return False

    for tile in moves:
        if not apply_move(board, tile, size):
            return False

    return is_solved(board, size)


def render_image(puzzle) -> Image.Image:
    """Render the puzzle's initial state as a PIL image."""
    board = json.loads(puzzle.text)
    size = int(len(board) ** 0.5)
    return render_board_image(board, size)


def render_board_image(board: list[int], size: int) -> Image.Image:
    """Render a board state as a PIL image with numbered tiles."""
    total = TILE_SIZE * size + TILE_GAP * (size + 1)
    image = Image.new("RGB", (total, total), color=BORDER_COLOR)
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(str(TEXT_FONT), FONT_SIZE)
    except OSError:
        font = ImageFont.load_default()

    for idx, tile in enumerate(board):
        r, c = divmod(idx, size)
        x = TILE_GAP + c * (TILE_SIZE + TILE_GAP)
        y = TILE_GAP + r * (TILE_SIZE + TILE_GAP)

        if tile == 0:
            draw.rectangle([x, y, x + TILE_SIZE, y + TILE_SIZE], fill=EMPTY_COLOR)
        else:
            draw.rectangle([x, y, x + TILE_SIZE, y + TILE_SIZE], fill=TILE_COLOR)
            cx = x + TILE_SIZE // 2
            cy = y + TILE_SIZE // 2
            draw.text((cx, cy), str(tile), font=font, fill=TILE_TEXT_COLOR, anchor="mm")

    return image

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import random

TEXT_FONT = Path(__file__).parent / "assets" / "FreeSerifBold.otf"

WIDTH = 5
HEIGHT = 4
TEXT_SIZE = 32
TEXT_PADDING = TEXT_SIZE
IGNORED_CHARS = "012345689"
COUNTED_CHAR = "7"

INPUT_TYPE = "number"
INPUT_HINT = f"count symbols {COUNTED_CHAR} in the matrix"


def set_globals(ignored_chars, counted_char, width, height, text_size):
    """Save everything in globals, if set in generate_puzzle_fields"""
    global IGNORED_CHARS
    global COUNTED_CHAR
    global WIDTH
    global HEIGHT
    global TEXT_SIZE
    IGNORED_CHARS = ignored_chars
    COUNTED_CHAR = counted_char
    WIDTH = width
    HEIGHT = height
    TEXT_SIZE = text_size


def generate_puzzle_fields(
    ignored_chars=IGNORED_CHARS,
    counted_char=COUNTED_CHAR,
    width=WIDTH,
    height=HEIGHT,
    text_size=TEXT_SIZE,
):
    """Create new puzzle for a player"""
    set_globals(ignored_chars, counted_char, width, height, text_size)
    rows = []
    for _ in range(height):

        row = "".join(random.choice(ignored_chars + counted_char) for i in range(width))
        rows.append(row)
    text = "\n".join(rows)

    return dict(text=text, solution=str(text.count(counted_char)))


def is_correct(response, puzzle):
    return puzzle.solution == response


def render_text(puzzle):
    """Return the digit matrix as plain text (rows of digits)."""
    return puzzle.text


def render_image(puzzle):
    font = ImageFont.truetype(str(TEXT_FONT), TEXT_SIZE)
    grid_c = TEXT_SIZE + TEXT_PADDING * 2
    grid_w = grid_c * WIDTH
    grid_h = grid_c * HEIGHT
    image = Image.new("RGB", (grid_w, grid_h))
    draw = ImageDraw.Draw(image)

    for rownum, row in enumerate(puzzle.text.split("\n")):
        for colnum, char in enumerate(row):
            x = colnum * grid_c
            y = rownum * grid_c
            mid = grid_c * 0.5
            draw.rectangle([x, y, x + grid_c, y + grid_c])
            draw.text((x + mid, y + mid), char, font=font, anchor="mm")

    return image

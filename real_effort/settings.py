from os import environ

SESSION_CONFIGS = [
    dict(
        name="count_numbers",
        display_name="Count Numbers",
        num_demo_participants=1,
        app_sequence=["count_numbers"],
        repetitions=3,
    ),
    dict(
        name="task_decoding",
        display_name="Word Decoding",
        num_demo_participants=1,
        app_sequence=["task_decoding"],
        repetitions=3,
    ),
    dict(
        name="task_sequences",
        display_name="Number Sequences",
        num_demo_participants=1,
        app_sequence=["task_sequences"],
        repetitions=3,
    ),
    dict(
        name="counting_zeros",
        display_name="Count Zeros",
        num_demo_participants=1,
        app_sequence=["counting_zeros"],
        repetitions=3,
    ),
    dict(
        name="task_summation",
        display_name="Summation Grid",
        num_demo_participants=1,
        app_sequence=["task_summation"],
        repetitions=3,
    ),
    dict(
        name="task_transcription",
        display_name="Text Transcription",
        num_demo_participants=1,
        app_sequence=["task_transcription"],
        repetitions=3,
    ),
    dict(
        name="add_numbers",
        display_name="Add Numbers",
        num_demo_participants=1,
        app_sequence=["add_numbers"],
        repetitions=3,
    ),
    dict(
        name="sudoku_game",
        display_name="Sudoku 6x6",
        num_demo_participants=1,
        app_sequence=["sudoku_game"],
        repetitions=3,
    ),
    dict(
        name="slider_puzzle",
        display_name="Slider Puzzle",
        num_demo_participants=1,
        app_sequence=["slider_puzzle"],
        repetitions=3,
    ),
    dict(
        name="string_entry",
        display_name="String Entry",
        num_demo_participants=1,
        app_sequence=["string_entry"],
        repetitions=3,
    ),
]

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.50, participation_fee=2.50, doc="")

PARTICIPANT_FIELDS = []
SESSION_FIELDS = ["params"]

LANGUAGE_CODE = "en"
REAL_WORLD_CURRENCY_CODE = "EUR"
USE_POINTS = True

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_INTRO_HTML = """ """
SECRET_KEY = "6962056274088"

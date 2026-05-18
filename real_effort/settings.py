from os import environ

SESSION_CONFIGS = [
    # ── Two-day human experiment — each room runs one of these ──
    # repetitions / incentive / timeouts all come from config/otree_config.yaml.
    dict(
        name="real_effort_day1",
        display_name="Artificial Effort — Day 1",
        num_demo_participants=1,
        app_sequence=[
            "intro",
            "string_entry",
            "counting_zeros",
            "add_numbers",
            "task_summation",
            "task_sequences",
        ],
    ),
    dict(
        name="real_effort_day2",
        display_name="Artificial Effort — Day 2",
        num_demo_participants=1,
        app_sequence=[
            "intro",
            "sudoku_game",
            "task_decoding",
            "task_transcription",
        ],
    ),
    # ── Individual games — selectable for piloting a single task ──
    dict(name="add_numbers", display_name="Add Numbers",
         num_demo_participants=1, app_sequence=["add_numbers"]),
    dict(name="counting_zeros", display_name="Count Zeros",
         num_demo_participants=1, app_sequence=["counting_zeros"]),
    dict(name="string_entry", display_name="String Entry",
         num_demo_participants=1, app_sequence=["string_entry"]),
    dict(name="task_summation", display_name="Summation Grid",
         num_demo_participants=1, app_sequence=["task_summation"]),
    dict(name="task_sequences", display_name="Number Sequences",
         num_demo_participants=1, app_sequence=["task_sequences"]),
    dict(name="sudoku_game", display_name="Sudoku 6x6",
         num_demo_participants=1, app_sequence=["sudoku_game"]),
    dict(name="task_decoding", display_name="Word Decoding",
         num_demo_participants=1, app_sequence=["task_decoding"]),
    dict(name="task_transcription", display_name="Text Transcription",
         num_demo_participants=1, app_sequence=["task_transcription"]),
]

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.50, participation_fee=2.50, doc="")

# Stable recruitment URLs — one per study day:
#   /room/real_effort_day1/   and   /room/real_effort_day2/
# Create a session "for" the room in the admin (config of the same name);
# participants who open the room link are auto-assigned a slot. Open rooms
# (no participant_label_file) — a ?participant_label=<id> query param is still
# recorded, but the same person's two days are linked by the email they enter.
ROOMS = [
    dict(name="real_effort_day1", display_name="Artificial Effort — Day 1"),
    dict(name="real_effort_day2", display_name="Artificial Effort — Day 2"),
]

PARTICIPANT_FIELDS = []
SESSION_FIELDS = ["params"]

LANGUAGE_CODE = "en"
REAL_WORLD_CURRENCY_CODE = "EUR"
USE_POINTS = True

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_INTRO_HTML = """ """
SECRET_KEY = environ.get("OTREE_SECRET_KEY", "6962056274088")

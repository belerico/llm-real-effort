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

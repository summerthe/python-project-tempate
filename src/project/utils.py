from pathlib import Path

from dotenv import dotenv_values


def set_env() -> dict[str, any]:
    """Set environment variables from .env file.

    Returns
    -------
    dict[str,any]
    """
    BASE_DIR = Path().resolve().parent
    ENV_PATH = BASE_DIR / ".env"
    env = dotenv_values(ENV_PATH)  # take environment variables from .env.
    return env

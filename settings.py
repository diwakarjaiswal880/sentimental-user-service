from pathlib import Path

from dotenv import load_dotenv

BASE_PATH = Path.cwd()
ENV_FILE_PATH = BASE_PATH / ".env"

load_dotenv(dotenv_path=ENV_FILE_PATH, verbose=True)


class DevelopmentConfig:
    pass

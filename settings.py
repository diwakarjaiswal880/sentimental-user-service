import os
from pathlib import Path

from dotenv import load_dotenv

BASE_PATH = Path.cwd()
ENV_FILE_PATH = BASE_PATH / ".env"

load_dotenv(dotenv_path=ENV_FILE_PATH, verbose=True)

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False

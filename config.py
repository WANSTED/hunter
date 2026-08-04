import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    DB_PATH: Path = Path(os.getenv("DB_PATH", "data/database.db"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    CHECK_INTERVAL: int = int(os.getenv("CHECK_INTERVAL", "300"))
    TIMEZONE: str = os.getenv("TIMEZONE", "UTC")

    @classmethod
    def validate(cls) -> None:
        if not cls.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is not configured")


config = Config()

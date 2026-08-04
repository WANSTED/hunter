from pathlib import Path

import aiosqlite

from config import config


class Database:
    def __init__(self, db_path: str | None = None):
        self.db_path = db_path or config.DB_PATH
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)

    async def connect(self):
        return aiosqlite.connect(self.db_path)

    async def init(self):
        async with await self.connect() as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    telegram_id INTEGER UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            await db.commit()

    async def execute(self, query: str, params: tuple = ()):
        async with await self.connect() as db:
            cursor = await db.execute(query, params)
            await db.commit()
            return cursor

    async def fetchone(self, query: str, params: tuple = ()):
        async with await self.connect() as db:
            cursor = await db.execute(query, params)
            return await cursor.fetchone()


 database = Database()

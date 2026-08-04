from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger


class Scheduler:
    """Background task scheduler for FreeHunter."""

    def __init__(self):
        self.scheduler = AsyncIOScheduler()

    def add_job(self, func, *args, **kwargs):
        """Register asynchronous background job."""
        self.scheduler.add_job(func, *args, **kwargs)

    def start(self):
        """Start scheduler."""
        if not self.scheduler.running:
            self.scheduler.start()
            logger.info("Scheduler started")

    async def shutdown(self):
        """Shutdown scheduler."""
        if self.scheduler.running:
            self.scheduler.shutdown(wait=False)
            logger.info("Scheduler stopped")


scheduler = Scheduler()

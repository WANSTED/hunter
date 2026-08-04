from abc import ABC, abstractmethod


class BaseService(ABC):
    """Base interface for FreeHunter services."""

    @abstractmethod
    async def start(self) -> None:
        """Initialize service resources."""
        raise NotImplementedError

    @abstractmethod
    async def stop(self) -> None:
        """Release service resources."""
        raise NotImplementedError

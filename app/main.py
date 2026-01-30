import asyncio
import logging

from core.bot import run
from core.config import settings

if __name__ == "__main__":
    logging.basicConfig(
        level=settings.logging.level,
        format=settings.logging.format,
        datefmt=settings.logging.datefmt,
    )
    asyncio.run(run(settings))

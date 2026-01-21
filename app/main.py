import asyncio

from core.bot import run
from core.config import settings

if __name__ == "__main__":
    asyncio.run(run(settings))

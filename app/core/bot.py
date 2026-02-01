from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.router import router


async def run(settings):
    bot = Bot(token=settings.bot.token, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(router)
    await dp.start_polling(bot)

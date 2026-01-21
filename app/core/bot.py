from aiogram import Bot, Dispatcher
from router import router


async def run(settings):
    bot = Bot(token=settings.bot.token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

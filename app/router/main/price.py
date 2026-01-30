from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from service.crypto.prices import top_crypto_handler

price_router = Router()


@price_router.message(Command("qwe"))
async def price_handler(message: Message):
    response = await top_crypto_handler()
    return message.answer(response)

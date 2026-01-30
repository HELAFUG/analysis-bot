from aiogram import F, Router
from aiogram.types import Message
from service.ethereum import get_current_gas_price_gwei

gas_router = Router(name="gas")


@gas_router.message(F.text == "/gas")
async def cmd_gas(msg: Message):
    try:
        gwei = get_current_gas_price_gwei()
        await msg.answer(f"Current ETH Gas: {gwei:.2f} Gwei")
    except Exception as e:
        await msg.answer(f"Error: {str(e)}")

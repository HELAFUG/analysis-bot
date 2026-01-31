from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from .gas import gas_router
from .price import price_router
from .rsi import rsi_router
from .signals import signal_router
from .top10 import top10_router

router = Router()
router.include_routers(
    signal_router, top10_router, price_router, gas_router, rsi_router
)


@router.message(CommandStart())
async def start(message: Message):
    welcome_text = (
        "<b>✦ Crypto Analysis Bot ✦</b>\n\n"
        "Real-time crypto data • TON wallet integration\n\n"
        "💎 <b>Core Commands</b>\n"
        "  /top10          Top 10 by market cap\n"
        "  /signal [coin]  Trading signal\n"
        "  /price [coin]   Current price\n"
        "  /rsi [coin]     14-day RSI\n\n"
        "🌐 <b>TON Wallet</b>\n"
        "  /connectwallet  Connect (@wallet, Tonkeeper…)\n"
        "  /balance        Check TON balance\n"
        "  /disconnect     Log out wallet\n\n"
        "<i>Start with /top10 or /connectwallet</i> • <code>/signal ton</code>"
    )

    await message.answer(welcome_text, parse_mode="HTML")

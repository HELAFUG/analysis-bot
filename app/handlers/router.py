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
    text = (
        "✨ **Welcome to Crypto Analysis Bot** ✨\n\n"
        "🚀 Your powerful crypto companion\n"
        "━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📌 **Available Commands**\n\n"
        "💎  /top10     → Top 10 cryptocurrencies by market cap\n"
        "📊  /signal    → Get trading signal (e.g. <code>/signal bitcoin</code>)\n"
        "⛽  /gas       → Current Ethereum gas prices\n"
        "💰  /price     → Real-time price of any coin (new!)\n"
        "📈  /rsi       → 14-period RSI analysis (new!)\n"
        "🔐  /addwallet → Connect your ETH wallet\n"
        "💼  /balance   → Check your wallet balance\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Start exploring with /top10 or try /signal btc 🔥"
    )

    await message.answer(text, parse_mode="Markdown")

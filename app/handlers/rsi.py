# handlers/rsi.py  (new)
from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from service.signals import calculate_rsi  # we'll add this function below

rsi_router = Router(name="rsi")


@rsi_router.message(Command("rsi"))
async def cmd_rsi(msg: Message, command: CommandObject):
    if not command.args:
        await msg.answer(
            "📊 <b>Usage:</b>\n"
            "<code>/rsi bitcoin</code>  or  <code>/rsi eth</code>\n\n"
            "Shows the 14-day RSI for the specified cryptocurrency.",
            parse_mode="HTML",
        )
        return

    coin = command.args.strip().lower()

    try:
        rsi = calculate_rsi(coin, period=14)

        if rsi < 30:
            status = "🟢 Oversold (< 30)"
            emoji = "📉"
        elif rsi > 70:
            status = "🔴 Overbought (> 70)"
            emoji = "📈"
        else:
            status = "⚪ Neutral"
            emoji = "📊"

        text = (
            f"<b>{coin.upper()} — 14-day RSI</b>\n\n"
            f"{emoji} <b>{rsi:.2f}</b>\n"
            f"Status: {status}\n\n"
            f"<i>Tip: RSI below 30 often signals potential buying opportunity\n"
            f"RSI above 70 may indicate possible pullback.</i>"
        )

        await msg.answer(text, parse_mode="HTML")

    except ValueError:
        await msg.answer(
            f"❌ Couldn't find data for <b>{coin.upper()}</b>\n"
            f"Make sure it's a valid ticker (bitcoin, eth, sol, etc.)",
            parse_mode="HTML",
        )
    except Exception as e:
        await msg.answer(
            f"⚠️ Error fetching RSI for <b>{coin.upper()}</b>\n{str(e)}",
            parse_mode="HTML",
        )

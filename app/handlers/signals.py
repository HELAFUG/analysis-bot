# handlers/signal.py
from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from service.signals import simple_moving_average_signal

signal_router = Router(name="signal")


@signal_router.message(Command("signal"))
async def cmd_signal(msg: Message, command: CommandObject):
    if not command.args:
        await msg.answer(
            "📈 <b>Usage:</b>\n"
            "<code>/signal bitcoin</code>\n"
            "<code>/signal eth</code>\n\n"
            "Generates a simple trend-based trading signal using price vs 14-day SMA.",
            parse_mode="HTML",
        )
        return

    coin = command.args.strip().lower()

    try:
        signal, rationale, price, sma = simple_moving_average_signal(coin)

        # Optional: add visual hint depending on signal
        signal_emoji = (
            "🟢 BUY"
            if "buy" in signal.lower()
            else "🔴 SELL"
            if "sell" in signal.lower()
            else "⚪ HOLD"
        )

        text = (
            f"<b>{coin.upper()} — Trading Signal</b>\n\n"
            f"{signal_emoji} <b>{signal}</b>\n\n"
            f"Current Price:  <b>${price:,.2f}</b>\n"
            f"14-day SMA:     <b>${sma:,.2f}</b>\n\n"
            f"<b>Rationale:</b>\n"
            f"{rationale}\n\n"
            f"<i>Simple MA crossover strategy • Not financial advice</i>"
        )

        await msg.answer(text, parse_mode="HTML")

    except ValueError:
        # Common for "coin not found" or invalid data
        await msg.answer(
            f"❌ <b>{coin.upper()}</b> not recognized\n"
            "Try: bitcoin, ethereum, solana, bnb, xrp, etc.",
            parse_mode="HTML",
        )

    except Exception as e:
        await msg.answer(
            f"⚠️ Error generating signal for <b>{coin.upper()}</b>\n{str(e)}",
            parse_mode="HTML",
        )

# handlers/top10.py
from aiogram import F, Router
from aiogram.types import Message
from service.coingecko import get_top_10_coins

top10_router = Router(name="top10")


@top10_router.message(F.text == "/top10")
async def cmd_top10(msg: Message):
    try:
        coins = get_top_10_coins()

        if not coins:
            await msg.answer("No data available right now. Try again later ⏳")
            return

        lines = [
            "🌍 <b>Top 10 Cryptocurrencies by Market Cap</b> (CoinGecko)\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        ]

        for i, c in enumerate(coins, 1):
            name = c.get("name", "Unknown")
            symbol = c.get("symbol", "?").upper()
            price = c.get("current_price", 0)
            change_24h = c.get("price_change_percentage_24h", 0)

            arrow = "🟢" if change_24h > 0 else "🔴" if change_24h < 0 else "⚪"
            change_str = f"{arrow} {change_24h:+.2f}%"

            # Optional: add rank emoji for top 3
            rank_emoji = (
                "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i:2}."
            )

            lines.append(
                f"{rank_emoji} <b>{name}</b> ({symbol})\n"
                f"   ${price:,.2f}    {change_str}\n"
            )

        # Optional footer
        lines.append(
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "<i>Updated live • Prices in USD • 24h change</i>"
        )

        await msg.answer("\n".join(lines), parse_mode="HTML")

    except Exception as e:
        error_text = str(e)[:180] + "…" if len(str(e)) > 180 else str(e)
        await msg.answer(
            f"⚠️ <b>Error fetching Top 10</b>\n"
            f"{error_text}\n\n"
            "<i>Please try again in a moment</i>",
            parse_mode="HTML",
        )

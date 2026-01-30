from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from core.web3 import cg

price_router = Router(name="price")


@price_router.message(Command("price"))
async def cmd_price(msg: Message, command: CommandObject):
    if not command.args:
        await msg.answer(
            "💰 <b>Usage:</b>\n"
            "<code>/price bitcoin</code>  or  <code>/price eth</code>\n\n"
            "Shows the current price in USD for the specified cryptocurrency.",
            parse_mode="HTML",
        )
        return

    coin = command.args.strip().lower()

    try:
        data = cg.get_coin_by_id(coin)
        price = data["market_data"]["current_price"]["usd"]

        # Optional: pull a few more useful fields if available
        change_24h = data["market_data"]["price_change_percentage_24h"]
        market_cap = data["market_data"]["market_cap"]["usd"]

        change_emoji = "📈" if change_24h >= 0 else "📉"
        change_text = f"{change_emoji} {change_24h:+.2f}% (24h)"

        text = (
            f"<b>{coin.upper()} — Current Price</b>\n\n"
            f"💵 <b>${price:,.2f}</b>\n"
            f"{change_text}\n\n"
            f"Market Cap: <b>${market_cap:,.0f}</b>\n\n"
            f"<i>Powered by CoinGecko • Data updates frequently</i>"
        )

        await msg.answer(text, parse_mode="HTML")

    except KeyError:
        # Common when coin not found or unexpected response structure
        await msg.answer(
            f"❌ Coin <b>{coin.upper()}</b> not found\n"
            "Try common names like: bitcoin, ethereum, solana, doge, etc.",
            parse_mode="HTML",
        )
    except Exception as e:
        await msg.answer(
            f"⚠️ Error fetching price for <b>{coin.upper()}</b>\n{str(e)}",
            parse_mode="HTML",
        )

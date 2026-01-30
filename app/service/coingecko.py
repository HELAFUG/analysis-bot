from typing import Any, Dict, List

from core.web3 import cg


def get_top_10_coins(vs_currency: str = "usd") -> List[Dict[str, Any]]:
    """Returns top 10 coins by market cap"""
    data = cg.get_coins_markets(
        vs_currency=vs_currency,
        order="market_cap_desc",
        per_page=10,
        page=1,
        sparkline=False,
        price_change_percentage="24h",
    )
    return data


def get_coin_price_history(
    coin_id: str, vs_currency: str = "usd", days: int = 14
) -> List[float]:
    """Returns list of prices (in USD) for the last N days"""
    market_chart = cg.get_coin_market_chart_by_id(
        id=coin_id.lower(), vs_currency=vs_currency, days=days, interval="daily"
    )
    return [price[1] for price in market_chart["prices"]]

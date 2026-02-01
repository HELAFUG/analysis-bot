# services/signals.py
from typing import Tuple

import numpy as np

from service.coingecko import get_coin_price_history  # assuming this function exists


def calculate_rsi(coin_id: str, period: int = 14) -> float:
    """
    Calculate 14-period RSI using simple moving average method
    (standard first approximation – many platforms use this for daily charts)
    """
    # We need period + 1 prices to calculate period differences
    prices = get_coin_price_history(
        coin_id, days=period + 10
    )  # extra days for better initial average

    if len(prices) < period + 1:
        raise ValueError(
            f"Insufficient price data for {coin_id} (got {len(prices)} points, need at least {period + 1})"
        )

    # Calculate price changes
    deltas = np.diff(prices)

    # Separate gains and losses
    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)

    # First averages (simple mean for the first period)
    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])

    # If we have more data, we could do smoothed averages (Wilder's method),
    # but for simplicity we're using the most recent period only (common approximation)
    if len(gains) > period:
        # Could implement full Wilder's smoothing here, but keeping it basic:
        avg_gain = np.mean(gains[-period:])
        avg_loss = np.mean(losses[-period:])

    if avg_loss == 0:
        return 100.0

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)  # pyright: ignore[reportReturnType]


def simple_moving_average_signal(
    coin_id: str, days: int = 14
) -> Tuple[str, str, float, float]:
    """
    Naive trading signal combining:
    - Price vs SMA (with small buffer)
    - RSI for overbought/oversold confirmation

    Returns: (signal_text, rationale_text, current_price, sma)
    """
    prices = get_coin_price_history(coin_id, days=days)

    if not prices or len(prices) < 2:
        raise ValueError(f"No sufficient price history for {coin_id}")

    current_price = prices[-1]
    sma = sum(prices) / len(prices)

    # Basic SMA position
    if current_price > sma * 1.015:
        base_signal = "🟢 BUY"
        sma_comment = f"Price (${current_price:,.2f}) > SMA (${sma:,.2f})"
    elif current_price < sma * 0.985:
        base_signal = "🔴 SELL"
        sma_comment = f"Price (${current_price:,.2f}) < SMA (${sma:,.2f})"
    else:
        base_signal = "⚪ HOLD"
        sma_comment = f"Price (${current_price:,.2f}) ≈ SMA (${sma:,.2f})"

    # RSI component
    try:
        rsi = calculate_rsi(coin_id, period=14)
        rsi_comment = f"RSI: {rsi:.2f}"

        if rsi < 30:
            rsi_interpretation = " (Oversold → stronger buy case)"
        elif rsi > 70:
            rsi_interpretation = " (Overbought → stronger sell case)"
        elif rsi < 40:
            rsi_interpretation = " (Approaching oversold)"
        elif rsi > 60:
            rsi_interpretation = " (Approaching overbought)"
        else:
            rsi_interpretation = ""

        # Combine signals (RSI can override or strengthen)
        if "BUY" in base_signal and rsi < 40:
            final_signal = "🟢 STRONG BUY"
        elif "SELL" in base_signal and rsi > 60:
            final_signal = "🔴 STRONG SELL"
        elif rsi < 30 and base_signal != "🔴 SELL":
            final_signal = "🟢 BUY (RSI Oversold)"
        elif rsi > 70 and base_signal != "🟢 BUY":
            final_signal = "🔴 SELL (RSI Overbought)"
        else:
            final_signal = base_signal

    except Exception as e:
        # If RSI fails (e.g. not enough data), fall back to SMA only
        rsi = None
        rsi_comment = ""
        rsi_interpretation = f" (RSI calculation failed: {str(e)})"
        final_signal = base_signal

    # Build rationale
    rationale = (
        f"Current price: ${current_price:,.2f}\n"
        f"{days}-day SMA: ${sma:,.2f}\n"
        f"{sma_comment}\n"
        f"{rsi_comment}{rsi_interpretation}"
    )

    return final_signal, rationale, current_price, sma


# Optional: very basic MACD approximation (for future extension)
def simple_macd_signal(
    coin_id: str, fast: int = 12, slow: int = 26, signal_period: int = 9
) -> str:
    """Very simplified MACD — not production ready, just for illustration"""
    prices = get_coin_price_history(coin_id, days=slow + signal_period + 5)
    if len(prices) < slow:
        return "⚠️ Not enough data for MACD"

    import numpy as np

    ema_fast = np.mean(prices[-fast:])  # rough approximation
    ema_slow = np.mean(prices[-slow:])
    macd_line = ema_fast - ema_slow

    # Very crude signal line
    macd_values = []  # would need historical MACD in real impl  # pyright: ignore[reportUnusedVariable, reportUnusedVariable, reportUnusedVariable, reportUnusedVariable, reportUnusedVariable, reportUnusedVariable]
    # ... skipped for simplicity

    return "MACD not fully implemented yet"

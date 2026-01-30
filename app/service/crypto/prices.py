from service.crypto import ABI, FEEDS, web3


def get_price(symbol):
    address = FEEDS[symbol]
    contract = web3.eth.contract(address=address, abi=ABI)  # pyright: ignore[reportArgumentType, reportCallIssue]
    latest_data = contract.functions.latestRoundData().call()
    price = latest_data[1] / 10**8  # Most feeds have 8 decimals
    return price


async def top_crypto_handler():
    # Fetch prices
    prices = []
    for symbol in FEEDS:
        try:
            price = get_price(symbol)
            prices.append(f"{symbol}: ${price:.2f}")
        except Exception as e:
            prices.append(f"{symbol}: Error fetching price - {str(e)}")

    # Simple signal (you can customize this, e.g., based on some logic)
    signal = "Market Signal: Neutral (Hold) - Based on current prices."

    # Compose response
    response = f"{signal}\n\nCurrent Top 10 Crypto Prices (USD):\n" + "\n".join(prices)

    return response

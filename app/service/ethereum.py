from web3 import Web3


def get_current_gas_price_gwei():
    w3 = Web3(Web3.HTTPProvider("https://ethereum-rpc.publicnode.com"))
    if not w3.is_connected():
        raise ConnectionError("Cannot connect to Ethereum node")

    wei = w3.eth.gas_price
    return w3.from_wei(wei, "gwei")  # pyright: ignore[reportReturnType]

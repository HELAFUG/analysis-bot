__all__ = ["web3", "ABI", "FEEDS"]


from core.config import settings
from web3 import Web3

web3 = Web3(Web3.HTTPProvider(settings.web3.infura_api.url))


ABI = [
    {
        "inputs": [],
        "name": "latestRoundData",
        "outputs": [
            {"internalType": "uint80", "name": "roundId", "type": "uint80"},
            {"internalType": "int256", "name": "answer", "type": "int256"},
            {"internalType": "uint256", "name": "startedAt", "type": "uint256"},
            {"internalType": "uint256", "name": "updatedAt", "type": "uint256"},
            {"internalType": "uint80", "name": "answeredInRound", "type": "uint80"},
        ],
        "stateMutability": "view",
        "type": "function",
    }
]


FEEDS = {
    "BTC": "0xF4030086522a5bEEa4988F8cA5b36dbC97bEE88c",
    "ETH": "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419",
    "USDT": "0x3E7d1EAB13ad0104d2750B8863b489D65364e32D",
    "BNB": "0x14e613AC84a31f709eadbdF89C6CC390fDc9540A",
    "XRP": "0xCed2660c6Dd1Ffd856A5A87967ec3eBE2d8e5e1f",
    "USDC": "0x8fFfFfd4AfB6115b954Bd326cbe7B4BA576818f6",
    "SOL": "0x4ffC43a60e009B551865A93d232E30Fce26ceB46",
    "TRX": "0x9477f0E5bfABaf253cacEE3c0834EB68BbFC65c7",
    "DOGE": "0x2465CeBe8B4882d4b99b99bfa192b2dd3A15d61d",
    "ADA": "0xAE48c91dF1fE419994FFDa27da110D5b4b1916D1",
}

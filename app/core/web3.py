from pycoingecko import CoinGeckoAPI
from web3 import Web3

from core.config import settings

w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{settings.web3.infura_api}"))
cg = CoinGeckoAPI()

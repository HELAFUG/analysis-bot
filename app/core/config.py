from os import getenv

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class BotConfig(BaseModel):
    token: str = getenv("BOT_TOKEN", "")


class LoggingConfig(BaseModel):
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    datefmt: str = "%Y-%m-%d %H:%M:%S"


class InfuraAPIConfig(BaseModel):
    api_key: str = getenv("INFURA_API_KEY", "")

    @property
    def url(self):
        return f"https://mainnet.infura.io/v3/{self.api_key}"


class Web3Config(BaseModel):
    infura_api: InfuraAPIConfig = InfuraAPIConfig()


class DBConfig(BaseModel):
    url: str = getenv("DB_URL", "sqlite:///analysis_bot.db")
    echo: bool = False


class TonWalletConfig(BaseModel):
    TON_CONNECT_MANIFEST = {
        "url": "t.me/cryptoronews_bot",  # or t.me/yourbot
        "name": "Crypto Analysis Bot",
        "iconUrl": "https://your-icon-url.png",
    }


class Settings(BaseSettings):
    bot: BotConfig = BotConfig()
    logging: LoggingConfig = LoggingConfig()
    web3: Web3Config = Web3Config()
    db: DBConfig = DBConfig()
    ton_wallet: TonWalletConfig = TonWalletConfig()


settings = Settings()

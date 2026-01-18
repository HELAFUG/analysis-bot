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


class Web3Config(BaseModel):
    pass


class Settings(BaseSettings):
    bot: BotConfig = BotConfig()
    logging: LoggingConfig = LoggingConfig()
    web3: Web3Config = Web3Config()


settings = Settings()

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from core.config import settings


class DBHelper:
    def __init__(self, cfg):
        self.engine = create_async_engine(
            url=cfg.db.url,
        )
        
        self.session_factory = async_sessionmaker(
            self.engine,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
        )


db_helper = DBHelper(settings)

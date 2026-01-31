from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    user_id: Mapped[int] = mapped_column(index=True)
    wallet_code: Mapped[str]

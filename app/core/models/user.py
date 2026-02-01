from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    user_id: Mapped[int] = mapped_column(index=True)
    subscribe_at: Mapped[datetime] = mapped_column(server_default=func.now())

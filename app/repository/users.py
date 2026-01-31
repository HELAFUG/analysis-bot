from typing import Optional

from core.models import User, db_helper
from sqlalchemy import select


async def create_user_wallet(user_id: int, wallet: int) -> Optional[User]:
    async with db_helper.session_factory() as session:
        new_user = User(user_id=user_id, wallet_code=wallet)
        session.add(new_user)
        await session.refresh(new_user)
        await session.commit()
        return new_user


async def get_user_wallet(wallet_code: int) -> Optional[User]:
    async with db_helper.session_factory() as session:
        query = select(User).where(User.wallet_code == wallet_code)
        user = await session.execute(query)
        return user.scalar_one_or_none()

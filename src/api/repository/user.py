from sqlmodel import select

from api.config.db import get_session
from api.scheme.user import User


def get_user_by_tg_id(tg_id: int) -> User | None:
    with get_session() as session:
        st = select(User).where(User.telegram_id == str(tg_id))
        user = session.exec(st).first()
        return user


def get_user_by_id(user_id: int) -> User | None:
    with get_session() as session:
        user = session.get(User, user_id)
        return user


def create_user(user: User) -> User:
    with get_session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


def update_user(user: User) -> User:
    with get_session() as session:
        user_db = session.merge(user)
        session.commit()
        return user_db

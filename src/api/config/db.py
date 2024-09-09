from contextlib import contextmanager

from sqlmodel import create_engine, Session, SQLModel

# noinspection PyUnresolvedReferences
import api.scheme.user
# noinspection PyUnresolvedReferences
import api.scheme.user_repo
from api.config.env import DB_CON_STR

engine = create_engine(DB_CON_STR)
SQLModel.metadata.create_all(engine)


@contextmanager
def get_session():
    with Session(engine) as session:
        yield session

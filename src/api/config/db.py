from contextlib import contextmanager

from sqlmodel import create_engine, Session

from api.config.env import DB_CON_STR
from api.scheme.user import *

engine = create_engine(DB_CON_STR)
SQLModel.metadata.create_all(engine)


@contextmanager
def get_session():
    with Session(engine) as session:
        yield session

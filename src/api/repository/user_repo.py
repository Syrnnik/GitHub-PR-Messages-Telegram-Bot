from sqlmodel import select

from api.config.db import get_session
from api.scheme.user_repo import UserRepo


def get_user_repo_by_ids(user_id: int, repo_id: int) -> UserRepo | None:
    with get_session() as session:
        st = select(UserRepo)
        st = st.where(UserRepo.user_id == user_id)
        st = st.where(UserRepo.repo_id == str(repo_id))
        user_repo = session.exec(st).first()
        return user_repo


def get_repo_users_by_repo_id(repo_id: int) -> list[UserRepo]:
    with get_session() as session:
        st = select(UserRepo)
        st = st.where(UserRepo.repo_id == str(repo_id))
        user_repos_list = list(session.exec(st).all())
        return user_repos_list


def create_user_repo(user_repo: UserRepo) -> UserRepo:
    with get_session() as session:
        session.add(user_repo)
        session.commit()
        session.refresh(user_repo)
        return user_repo

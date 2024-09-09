from sqlmodel import SQLModel, Field


class UserRepo(SQLModel, table=True):
    __tablename__ = "user_repo"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    repo_id: str

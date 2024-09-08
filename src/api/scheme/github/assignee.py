from pydantic import BaseModel


class Assignee(BaseModel):
    login: str

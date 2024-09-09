from pydantic import BaseModel


class Repository(BaseModel):
    id: int
    full_name: str

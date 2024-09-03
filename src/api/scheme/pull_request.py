from pydantic import BaseModel


class PullRequest(BaseModel):
    action: str
    pull_request: dict

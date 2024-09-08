from pydantic import BaseModel

from api.scheme.github.assignee import Assignee


class PullRequest(BaseModel):
    body: str | None
    html_url: str
    assignee: Assignee | None

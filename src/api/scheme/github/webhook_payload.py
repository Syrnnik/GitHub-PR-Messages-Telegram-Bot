from pydantic import BaseModel

from api.scheme.github.pull_request import PullRequest
from api.scheme.github.repository import Repository


class WebhookPayload(BaseModel):
    action: str
    number: int
    pull_request: PullRequest
    repository: Repository

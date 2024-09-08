from pydantic import BaseModel

from api.scheme.github.pull_request import PullRequest


class WebhookPayload(BaseModel):
    action: str
    number: int
    pull_request: PullRequest

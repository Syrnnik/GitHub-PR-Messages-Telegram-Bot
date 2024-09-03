from fastapi import APIRouter

from api.scheme.pull_request import PullRequest
from bot.utils.pull_request_message import create_pull_request_message

router = APIRouter()


@router.post("/pull_request_webhook")
async def pull_request_webhook(payload: PullRequest):
    if payload.action == "opened":
        url = payload.pull_request['html_url']
        description = payload.pull_request['body']
        pull_request_message = create_pull_request_message(
            pull_request_url=url,
            description=description
        )

    return {"status": "success"}

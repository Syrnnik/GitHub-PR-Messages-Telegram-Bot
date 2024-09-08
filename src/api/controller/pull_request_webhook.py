from aiogram.enums import ParseMode
from fastapi import APIRouter

from api.config.env import ADMIN_TG_ID
from api.scheme.github.webhook_payload import WebhookPayload
from api.util.pull_request_message import create_pull_request_message
from bot.configs.loader import bot
from bot.keyboards.inline.add_task import get_add_task_inline_keyboard

router = APIRouter()


@router.post("")
async def pull_request_webhook(payload: WebhookPayload):
    pull_request = payload.pull_request

    url = pull_request.html_url
    description = pull_request.body
    assignee = pull_request.assignee
    by_user = assignee.login if assignee is not None else None

    pull_request_message_text = create_pull_request_message(
        pull_request_url=url,
        pull_request_body=description,
        by_user=by_user,
    )

    keyboard = get_add_task_inline_keyboard()

    await bot.send_message(
        chat_id=ADMIN_TG_ID,
        text=pull_request_message_text,
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )

    return {"status": "success"}

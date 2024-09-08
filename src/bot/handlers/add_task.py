from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from api.util.pull_request_message import create_pull_request_message
from bot.configs.loader import bot
from bot.states.user import UserState

router = Router()


@router.message(UserState.add_task)
async def add_task(message: Message, state: FSMContext):
    await message.delete()

    chat_id = message.chat.id

    state_data = await state.get_data()
    pull_request_message_id = state_data.get("message_id")

    answer_message_id = state_data.get("answer_message_id")
    await bot.delete_message(
        chat_id=chat_id,
        message_id=answer_message_id,
    )

    url = state_data.get("pull_request_url")
    description = state_data.get("pull_request_body")
    by_user = state_data.get("pull_request_user")
    task_url = message.text

    new_pull_request_message_text = create_pull_request_message(
        pull_request_url=url,
        pull_request_body=description,
        by_user=by_user,
        task_url=task_url,
    )

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=pull_request_message_id,
        text=new_pull_request_message_text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )
    await state.clear()

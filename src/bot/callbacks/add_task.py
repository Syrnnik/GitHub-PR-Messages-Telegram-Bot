from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.states.user import UserState

router = Router()


@router.callback_query(F.data.startswith("add_task"))
async def add_task(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    await state.set_state(UserState.task_add)

    answer_message = await callback.message.answer(
        text=f"Напиши мне ссылку на таску и я добавлю её в сообщение",
    )
    pull_request_message = callback.message
    entities = pull_request_message.entities
    message_urls = [entity.url for entity in entities if entity.type == "text_link"]
    url = message_urls[0] if len(message_urls) > 0 else None

    message_parts = pull_request_message.text.split("\n\n")
    description = message_parts[1]
    by_user = message_parts[0].split("by ")[1]

    message_id = callback.message.message_id
    answer_message_id = answer_message.message_id
    await state.set_data({
        "message_id": message_id,
        "answer_message_id": answer_message_id,
        "pull_request_url": url,
        "pull_request_body": description,
        "pull_request_user": by_user,
    })

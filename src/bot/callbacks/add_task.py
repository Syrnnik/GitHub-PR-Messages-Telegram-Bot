from aiogram import F, Router
from aiogram.enums.message_entity_type import MessageEntityType
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from api.util.pull_request_message import apply_entities_to_text
from bot.states.user import UserState

router = Router()


@router.callback_query(F.data.startswith("add_task"))
async def add_task(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    await state.set_state(UserState.add_task)

    answer_message = await callback.message.answer(
        text=f"Напиши мне ссылку на таску и я добавлю её в сообщение",
    )
    pull_request_message = callback.message
    entities = pull_request_message.entities
    message_urls = [entity.url for entity in entities if entity.type == MessageEntityType.TEXT_LINK]
    url = message_urls[0] if len(message_urls) > 0 else None

    message_text = pull_request_message.text
    message_text_md = apply_entities_to_text(
        text=pull_request_message.text,
        entities=entities,
    )

    message_md_parts = message_text_md.split("\n\n")
    message_parts = message_text.split("\n\n")

    description = None
    if len(message_md_parts) > 1:
        description = message_md_parts[1]

    by_user = None
    if len(message_parts) > 0:
        by_user_parts = message_parts[0].split("by ")
        if len(by_user_parts) > 1:
            by_user = by_user_parts[1]

    message_id = callback.message.message_id
    answer_message_id = answer_message.message_id
    await state.update_data({
        "message_id": message_id,
        "answer_message_id": answer_message_id,
        "pull_request_url": url,
        "pull_request_body": description,
        "pull_request_user": by_user,
    })

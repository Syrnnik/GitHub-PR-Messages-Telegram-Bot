from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from api.repository.user import get_user_by_tg_id
from bot.constants.bot_commands import start_command
from bot.keyboards.inline.authorize import get_github_auth_inline_keyboard

start_router = Router(name=__name__)


@start_router.message(Command(start_command))
async def start(message: Message, state: FSMContext):
    await state.clear()

    user_id = message.from_user.id

    user = get_user_by_tg_id(user_id)
    if not user:
        keyboard = get_github_auth_inline_keyboard(user_id)

        await message.answer(
            f"Привет! Авторизуйся через GitHub, чтобы мы продолжили",
            reply_markup=keyboard,
        )

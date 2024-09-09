from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.constants.bot_commands import authorize_command
from bot.keyboards.inline.authorize import get_github_auth_inline_keyboard

router = Router()


@router.message(Command(authorize_command))
async def authorize(message: Message, state: FSMContext):
    await state.clear()

    user_id = message.chat.id
    keyboard = get_github_auth_inline_keyboard(user_id)

    await message.answer(
        f"Привет! Авторизуйся через GitHub, чтобы мы продолжили",
        reply_markup=keyboard,
    )

from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from api.repository.user import get_user_by_tg_id
from bot.constants.bot_commands import start_command, select_repo_command
from bot.keyboards.inline.authorize import get_github_auth_inline_keyboard
from bot.keyboards.inline.select_repo import get_select_repo_inline_keyboard

router = Router()


@router.message(Command(start_command))
async def start(message: Message, state: FSMContext):
    await state.clear()

    user_id = message.chat.id

    user = get_user_by_tg_id(user_id)
    if not user:
        keyboard = get_github_auth_inline_keyboard(user_id)

        await message.answer(
            f"Привет! Авторизуйся через GitHub, чтобы мы продолжили",
            reply_markup=keyboard,
        )
    else:
        keyboard = get_select_repo_inline_keyboard()

        select_repo_command_text = select_repo_command.command.replace('_', r'\_')
        message_parts = [
            "*Ты уже авторизовался через GitHub*",
            f"\nЕсли хочешь подключить свои репозитории, то напиши /{select_repo_command_text}",
            f"или нажми на кнопку под этим сообщением"
        ]
        message_text = " ".join(message_parts)

        await message.answer(
            text=message_text,
            reply_markup=keyboard,
            parse_mode=ParseMode.MARKDOWN,
        )

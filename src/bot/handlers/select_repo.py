from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from api.repository.user import get_user_by_tg_id
from bot.configs.gh import get_user_github, get_user_repos_list
from bot.constants.bot_commands import select_repo_command
from bot.keyboards.reply.repos_list import get_repos_list_inline_keyboard
from bot.states.user import UserState

router = Router()


@router.message(Command(select_repo_command) or UserState.select_repo)
async def repos_list(message: Message, state: FSMContext):
    await state.set_state(UserState.repos_list)

    user_id = message.from_user.id
    user = get_user_by_tg_id(user_id)
    gh = get_user_github(user.github_access_token)
    repos_list = get_user_repos_list(gh)

    keyboard = get_repos_list_inline_keyboard(repos_list)

    await message.answer(
        f"Выбери репозиторий, с которого хочешь получать сообщения",
        reply_markup=keyboard,
    )

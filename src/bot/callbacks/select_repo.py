from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from api.repository.user import get_user_by_tg_id
from bot.configs.gh import get_user_github, get_user_repos_list
from bot.keyboards.reply.repos_list import get_repos_list_inline_keyboard
from bot.states.user import UserState

router = Router()


@router.callback_query(F.data.startswith("select_repo"))
async def select_repo(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(UserState.repos_list)

    user_id = callback.from_user.id
    user = get_user_by_tg_id(user_id)
    gh = get_user_github(user.github_access_token)
    repos_list = get_user_repos_list(gh)

    keyboard = get_repos_list_inline_keyboard(repos_list)

    await callback.message.answer(
        f"Выбери репозиторий, с которого хочешь получать сообщения",
        reply_markup=keyboard,
    )

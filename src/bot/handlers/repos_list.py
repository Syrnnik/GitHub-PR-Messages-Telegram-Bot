from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from api.repository.user import get_user_by_tg_id
from bot.configs.gh import get_user_github, create_repo_hook, get_repo_hook_by_name
from bot.states.user import UserState

router = Router()


@router.message(UserState.repos_list)
async def repos_list(message: Message, state: FSMContext):
    await state.clear()

    selected_repo = message.text

    user_id = message.from_user.id
    user = get_user_by_tg_id(user_id)
    gh = get_user_github(user.github_access_token)

    hook = get_repo_hook_by_name(gh, selected_repo)
    if hook:
        await message.answer(f"Ты уже получаешь сообщения с этого репозитория")
    else:
        create_repo_hook(gh, selected_repo)
        await message.answer(
            f"Хорошо, теперь я буду присылать тебе сообщения с пулл реквестами с этого репозитория"
        )

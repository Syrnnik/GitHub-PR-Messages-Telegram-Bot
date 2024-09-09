from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from api.repository.user import get_user_by_tg_id, get_user_by_id
from api.repository.user_repo import create_user_repo, get_repo_users_by_repo_id
from api.scheme.user_repo import UserRepo
from bot.configs.gh import get_user_github, get_repo_hook_by_name, get_repo_by_name, create_repo_hook
from bot.states.user import UserState

router = Router()


@router.message(UserState.repos_list)
async def repos_list(message: Message, state: FSMContext):
    await state.clear()

    selected_repo = message.text
    repo_name = selected_repo.split("/")[1]

    chat_id = message.chat.id
    user = get_user_by_tg_id(chat_id)
    user_id = user.id
    gh = get_user_github(user.github_access_token)

    repo = get_repo_by_name(gh, repo_name)
    repo_id = repo.id

    is_repo_connected = False
    repo_users_list = get_repo_users_by_repo_id(repo_id)
    for repo in repo_users_list:
        repo_user = get_user_by_id(repo.user_id)
        if repo_user.telegram_id == str(chat_id):
            is_repo_connected = True
            break

    hook = get_repo_hook_by_name(gh, selected_repo)

    if hook and is_repo_connected:
        await message.answer(f"Ты уже получаешь сообщения с этого репозитория")
    else:
        if not is_repo_connected:
            user_repo = UserRepo(
                user_id=user_id,
                repo_id=repo_id,
            )
            create_user_repo(user_repo)

        if not hook:
            create_repo_hook(gh, selected_repo)

        await message.answer(
            f"Хорошо, теперь я буду присылать тебе сообщения с пулл реквестами с этого репозитория"
        )

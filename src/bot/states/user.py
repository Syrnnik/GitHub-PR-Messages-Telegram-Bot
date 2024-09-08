from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    signin_in_github = State()

    select_repo = State()
    repos_list = State()

    add_task = State()

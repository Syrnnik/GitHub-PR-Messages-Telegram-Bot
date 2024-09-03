from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    signin_in_github = State()

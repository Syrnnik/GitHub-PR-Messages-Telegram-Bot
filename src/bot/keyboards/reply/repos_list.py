from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton


def get_repos_list_inline_keyboard(repos_list: list[str]):
    builder = ReplyKeyboardBuilder()
    for repo in repos_list:
        builder.row(
            KeyboardButton(text=f"{repo}")
        )
    keyboard = builder.as_markup()
    return keyboard

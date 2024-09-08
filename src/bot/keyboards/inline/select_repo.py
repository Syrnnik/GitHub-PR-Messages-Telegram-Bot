from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_select_repo_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Подключить репозиторий", callback_data="select_repo")
    keyboard = builder.as_markup()
    return keyboard

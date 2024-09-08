from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.configs.env import GITHUB_OAUTH_REDIRECT_URI, GITHUB_OAUTH_CLIENT_ID


def get_add_task_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить ссылку на таску", callback_data="add_task")
    keyboard = builder.as_markup()
    return keyboard

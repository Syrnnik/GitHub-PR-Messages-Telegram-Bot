from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.configs.env import GITHUB_OAUTH_REDIRECT_URI, GITHUB_OAUTH_CLIENT_ID


def get_github_auth_inline_keyboard(user_id: int):
    github_auth_url = (
        f"https://github.com/login/oauth/authorize?client_id={GITHUB_OAUTH_CLIENT_ID}"
        f"&redirect_uri={GITHUB_OAUTH_REDIRECT_URI}&state={user_id}"
    )

    builder = InlineKeyboardBuilder()
    builder.button(text="Авторизоваться", url=github_auth_url)
    keyboard = builder.as_markup()
    return keyboard

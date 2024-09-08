from aiogram import Dispatcher

from bot.callbacks import all_callback_routers
from bot.handlers import all_handler_routers


def set_bot_routers(dispatcher: Dispatcher):
    dispatcher.include_routers(
        *all_handler_routers,
        *all_callback_routers,
    )

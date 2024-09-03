from aiogram import Bot

from bot.constants.bot_commands import start_command


async def set_bot_commands(bot: Bot):
    await bot.set_my_commands([
        start_command,
    ])

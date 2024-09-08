from aiogram import Bot

from bot.constants.bot_commands import all_bot_commands


async def set_bot_commands(bot: Bot):
    await bot.set_my_commands(all_bot_commands)

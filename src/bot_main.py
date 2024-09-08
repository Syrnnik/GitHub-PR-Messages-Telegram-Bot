import asyncio

from aiogram import Bot
from loguru import logger

from bot.configs.loader import dp, bot
from bot.utils.bot.commands import set_bot_commands
from bot.utils.bot.routers import set_bot_routers


async def on_startup(bot: Bot):
    await set_bot_commands(bot)

    bot_data = await bot.me()
    logger.success(f"{bot_data.first_name} is ready!")


async def main():
    set_bot_routers(dp)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.constants.bot_commands import login_command
from bot.keyboards.inline import example_inline_keyboard
from bot.keyboards.reply.example import example_reply_keyboard
from bot.states.user import UserState

start_router = Router(name=__name__)


@start_router.message(Command(login_command))
async def login(message: Message, state: FSMContext):
    # Set user state
    await state.set_state(UserState.logging)

    # Answer to user message
    # With inline keyboard
    await message.answer("Hello!", reply_markup=example_inline_keyboard)
    # With reply keyboard
    await message.answer("I am bot..", reply_markup=example_reply_keyboard)

from aiogram.types import BotCommand

start_command = BotCommand(
    command="start",
    description="Start chat with bot"
)

select_repo_command = BotCommand(
    command="select_repo",
    description="Select github repo to get Pull Request messages"
)

authorize_command = BotCommand(
    command="authorize",
    description="Authorize in bot using GitHub"
)

all_bot_commands = [
    start_command,
    select_repo_command,
    authorize_command,
]

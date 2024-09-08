from bot.handlers import start
from bot.handlers import add_task

all_handler_routers = [
    start.router,
    add_task.router,
]

from bot.handlers import add_task
from bot.handlers import authorize
from bot.handlers import repos_list
from bot.handlers import select_repo
from bot.handlers import start

all_handler_routers = [
    authorize.router,
    start.router,
    add_task.router,
    select_repo.router,
    repos_list.router,
]

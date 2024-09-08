from bot.callbacks import add_task
from bot.callbacks import select_repo

all_callback_routers = [
    add_task.router,
    select_repo.router,
]

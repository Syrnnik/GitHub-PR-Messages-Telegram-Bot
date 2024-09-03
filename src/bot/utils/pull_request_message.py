def create_pull_request_message(
    pull_request_url: str,
    description: str,
    task_url: str | None = None
) -> str:
    description = description.replace("## Выполнено\r\n", "")

    if task_url:
        pull_request_message = f"[ПР]({pull_request_url})  --  [Таска]({task_url})\n\n{description}"
    else:
        pull_request_message = f"[ПР]({pull_request_url})\n\n{description}"

    return pull_request_message

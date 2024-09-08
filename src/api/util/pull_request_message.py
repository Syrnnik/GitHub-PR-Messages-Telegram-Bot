def create_pull_request_message(
    pull_request_url: str,
    pull_request_body: str | None,
    by_user: str | None,
    task_url: str | None = None,
) -> str:
    pull_request = f"<b><a href='{pull_request_url}'>ПР</a></b>"

    task = ""
    if task_url is not None:
        task = f" <b>—</b>  <b><a href='{task_url}'>Таска</a></b>"

    done_by = ""
    if by_user is not None:
        done_by = f" <i>by {by_user}</i>"

    description = ""
    if pull_request_body is not None:
        description = f"\n\n{pull_request_body}"

    message_parts = [
        pull_request,
        task,
        done_by,
        description
    ]
    message_parts = [
        part for part in message_parts if part
    ]

    pull_request_message = " ".join(message_parts)

    return pull_request_message

import re

from aiogram.enums import MessageEntityType
from aiogram.types import MessageEntity


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
        description = f"\n\n{markdown_to_html(pull_request_body)}"

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


def markdown_to_html(markdown_text: str) -> str:
    # Заменяем жирный текст
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown_text)

    # Заменяем курсивный текст
    markdown_text = re.sub(r'_(.*?)_', r'<i>\1</i>', markdown_text)

    # Заменяем код
    markdown_text = re.sub(r'`(.*?)`', r'<code>\1</code>', markdown_text)

    # Заменяем ссылки
    markdown_text = re.sub(r'\[([^]]+)]\(([^)]+)\)', r'<a href="\2">\1</a>', markdown_text)

    # Заменяем изображения
    markdown_text = re.sub(r'!\[([^]]*)]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', markdown_text)

    return markdown_text


def apply_entities_to_text(text: str, entities: list[MessageEntity]) -> str:
    """
    Применяет MessageEntity к тексту и возвращает строку в MarkdownV2.
    """
    # Сортируем entities по возрастанию позиции
    entities = sorted(entities, key=lambda e: e.offset)

    # Создаем список сегментов текста и их разметки
    segments = []
    last_pos = 0

    for entity in entities:
        # Добавляем текст до текущей entity
        if entity.offset > last_pos:
            segments.append(text[last_pos:entity.offset])

        # Определяем разметку для текущей entity
        if entity.type == MessageEntityType.BOLD:
            segments.append(f"**{text[entity.offset:entity.offset + entity.length]}**")
        elif entity.type == MessageEntityType.ITALIC:
            segments.append(f"_{text[entity.offset:entity.offset + entity.length]}_")
        elif entity.type == MessageEntityType.CODE:
            segments.append(f"`{text[entity.offset:entity.offset + entity.length]}`")
        elif entity.type == MessageEntityType.TEXT_LINK:
            url = entity.url
            segments.append(f"[{text[entity.offset:entity.offset + entity.length]}]({url})")

        last_pos = entity.offset + entity.length

    # Добавляем оставшийся текст
    if last_pos < len(text):
        segments.append(text[last_pos:])

    # Объединяем все сегменты
    markdown_text = ''.join(segments)

    return markdown_text

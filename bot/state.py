"""Тимчасові дані користувачів і тестове нагадування."""

import asyncio
from datetime import datetime

users = {}
reminder_tasks = {}


def get_name(message) -> str:
    """Повернути ім'я користувача."""
    return message.from_user.first_name or "друже"


def ensure_user(user_id: int, name: str) -> None:
    """Створити користувача в пам'яті."""
    if user_id not in users:
        users[user_id] = {
            "name": name,
            "training": False,
            "walk": False,
            "food": False,
            "streak": 0,
            "last_training": None,
            "last_walk": None,
            "last_food": None,
        }


def mark(user_id: int, key: str, date_key: str) -> bool:
    """Відмітити дію за сьогодні."""
    today = datetime.now().date().isoformat()
    if users[user_id][date_key] == today:
        return False
    users[user_id][key] = True
    users[user_id][date_key] = today
    return True


def mark_training(user_id: int) -> bool:
    """Відмітити тренування."""
    ok = mark(user_id, "training", "last_training")
    if ok:
        users[user_id]["streak"] += 1
        cancel_test_reminder(user_id)
    return ok


def mark_walk(user_id: int) -> bool:
    """Відмітити прогулянку."""
    return mark(user_id, "walk", "last_walk")


def mark_food(user_id: int) -> bool:
    """Відмітити харчування."""
    return mark(user_id, "food", "last_food")


def get_streak(user_id: int) -> int:
    """Повернути серію."""
    return users[user_id]["streak"]


def cancel_test_reminder(user_id: int) -> None:
    """Скасувати попереднє тестове нагадування для користувача."""
    task = reminder_tasks.get(user_id)
    if task and not task.done():
        task.cancel()


async def send_test_training_reminder(bot, user_id: int):
    """Через 1 хвилину надіслати тестове нагадування, якщо тренування не відмічено."""
    try:
        await asyncio.sleep(60)

        if user_id not in users:
            return

        user = users[user_id]

        if not user["training"]:
            text = (
                f"{user['name']}, час для руху 🏃\n\n"
                "Якщо сьогодні ще не було тренування — можна почати навіть з 5 хвилин 💪"
            )
            await bot.send_message(chat_id=user_id, text=text)
    except asyncio.CancelledError:
        pass
    finally:
        reminder_tasks.pop(user_id, None)


def start_test_reminder(bot, user_id: int) -> None:
    """Запустити одне тестове нагадування і скасувати попереднє, якщо воно було."""
    cancel_test_reminder(user_id)
    reminder_tasks[user_id] = asyncio.create_task(
        send_test_training_reminder(bot, user_id)
    )
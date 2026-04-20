"""Тексти бота."""

import random

WELCOME_TEXT = (
    "Привіт, {name}! 👋\n\n"
    "Я бот корисних звичок 💪"
)

HELP_TEXT = (
    "❓ Як користуватись ботом:\n"
    "🏃 Тренування — відмітити тренування\n"
    "🚶 Прогулянка — відмітити прогулянку\n"
    "🥗 Харчування — відмітити харчування\n"
    "🔥 Моя серія — подивитись серію\n"
    "💬 Мотивація — отримати підтримку"
)

TRAINING_DONE = [
    "🏃 Тренування відмічено, {name}!",
    "✅ Активність записано, {name}!"
]

WALK_DONE = [
    "🚶 Прогулянку відмічено, {name}!",
    "✅ Активність записано, {name}!"
]

FOOD_DONE = [
    "🥗 Харчування відмічено, {name}!",
    "✅ Режим записано, {name}!"
]

MOTIVATIONS = [
    "Навіть маленький крок — це вже рух уперед ✨",
    "Регулярність сильніша за ідеальний план 💪",
    "Турбота про себе має значення 🌿"
]

ALREADY_DONE = "Цю дію вже відмічено сьогодні ✅"
FALLBACK_TEXT = "Скористайся кнопками меню 😊"
REMINDER_TEXT = "{name}, нагадую про тренування 🏃"
SERIES_TEXT = "🔥 {name}, поточна серія: {days} дн."


def pick_training(name: str) -> str:
    """Повернути текст для тренування."""
    return random.choice(TRAINING_DONE).format(name=name)


def pick_walk(name: str) -> str:
    """Повернути текст для прогулянки."""
    return random.choice(WALK_DONE).format(name=name)


def pick_food(name: str) -> str:
    """Повернути текст для харчування."""
    return random.choice(FOOD_DONE).format(name=name)


def pick_motivation() -> str:
    """Повернути мотивацію."""
    return random.choice(MOTIVATIONS)
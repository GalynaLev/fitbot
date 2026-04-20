"""Головне меню бота."""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_menu() -> ReplyKeyboardMarkup:
    """Повернути клавіатуру меню."""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🏃 Тренування"), KeyboardButton(text="🚶 Прогулянка")],
            [KeyboardButton(text="🥗 Харчування"), KeyboardButton(text="🔥 Моя серія")],
            [KeyboardButton(text="💬 Мотивація"), KeyboardButton(text="❓ Допомога")],
            
        ],
        resize_keyboard=True,
        input_field_placeholder="Обери дію 👇"
    )
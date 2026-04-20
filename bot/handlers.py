"""Усі обробники бота."""

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.menu import get_menu
from bot.state import (
    ensure_user,
    get_name,
    mark_training,
    mark_walk,
    mark_food,
    get_streak,
    start_test_reminder,
)
from bot.texts import (
    WELCOME_TEXT,
    HELP_TEXT,
    ALREADY_DONE,
    FALLBACK_TEXT,
    SERIES_TEXT,
    pick_training,
    pick_walk,
    pick_food,
    pick_motivation,
)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Обробити /start."""
    name = get_name(message)
    ensure_user(message.from_user.id, name)

    await message.answer(
        WELCOME_TEXT.format(name=name),
        reply_markup=get_menu()
    )

    start_test_reminder(message.bot, message.from_user.id)


@router.message(F.text == "🏃 Тренування")
async def training_handler(message: Message):
    """Обробити кнопку тренування."""
    name = get_name(message)
    ensure_user(message.from_user.id, name)

    text = pick_training(name) if mark_training(message.from_user.id) else ALREADY_DONE
    await message.answer(text, reply_markup=get_menu())


@router.message(F.text == "🚶 Прогулянка")
async def walk_handler(message: Message):
    """Обробити кнопку прогулянки."""
    name = get_name(message)
    ensure_user(message.from_user.id, name)

    text = pick_walk(name) if mark_walk(message.from_user.id) else ALREADY_DONE
    await message.answer(text, reply_markup=get_menu())


@router.message(F.text == "🥗 Харчування")
async def food_handler(message: Message):
    """Обробити кнопку харчування."""
    name = get_name(message)
    ensure_user(message.from_user.id, name)

    text = pick_food(name) if mark_food(message.from_user.id) else ALREADY_DONE
    await message.answer(text, reply_markup=get_menu())


@router.message(F.text == "🔥 Моя серія")
async def streak_handler(message: Message):
    """Показати серію."""
    name = get_name(message)
    ensure_user(message.from_user.id, name)

    await message.answer(
        SERIES_TEXT.format(name=name, days=get_streak(message.from_user.id)),
        reply_markup=get_menu()
    )


@router.message(F.text == "💬 Мотивація")
async def motivation_handler(message: Message):
    """Надіслати мотивацію."""
    name = get_name(message)
    ensure_user(message.from_user.id, name)

    await message.answer(
        f"{name}, {pick_motivation()}",
        reply_markup=get_menu()
    )


@router.message(F.text == "❓ Допомога")
async def help_handler(message: Message):
    """Показати допомогу."""
    await message.answer(HELP_TEXT, reply_markup=get_menu())


@router.message()
async def fallback_handler(message: Message):
    """Обробити невідомий текст."""
    await message.answer(FALLBACK_TEXT, reply_markup=get_menu())
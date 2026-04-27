"""Робота з JSON-базою."""

import json
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent / "data.json"


def load_data() -> dict:
    """Завантажити дані з JSON."""
    if not DB_PATH.exists():
        return {}

    try:
        with open(DB_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}


def save_data(data: dict) -> None:
    """Зберегти дані в JSON."""
    with open(DB_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
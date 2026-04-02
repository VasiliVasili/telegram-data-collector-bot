from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from config import ADMIN_IDS

router = Router()

@router.message(Command("leads"))
async def get_leads(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        return

    try:
        with open("data.csv", "r", encoding="utf-8") as f:
            lines = f.readlines()[-5:]  # последние 5 заявок

        text = "Последние заявки:\n\n" + "".join(lines)

    except FileNotFoundError:
        text = "Нет заявок."

    await message.answer(text)
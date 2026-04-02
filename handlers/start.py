from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.main_menu import main_menu_kb

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Добро пожаловать! Выберите действие:",
        reply_markup=main_menu_kb()
    )
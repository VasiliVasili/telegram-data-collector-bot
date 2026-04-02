from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Оставить заявку")],
            [KeyboardButton(text="Контакты")]
        ],
        resize_keyboard=True
    )
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from config import ADMIN_IDS

from states.form_states import Form
from services.csv_service import save_to_csv
from services.sheets_service import save_to_sheets

router = Router()

@router.message(lambda message: message.text == "Оставить заявку")
async def start_form(message: Message, state: FSMContext):
    await message.answer("Введите ваше имя:")
    await state.set_state(Form.name)

@router.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите телефон:")
    await state.set_state(Form.phone)

@router.message(Form.phone)
async def process_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Комментарий:")
    await state.set_state(Form.comment)

@router.message(Form.comment)
async def process_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    data = await state.get_data()

    save_to_csv(data)
    save_to_sheets(data)

    # --- уведомление админу ---
    text = (
        "📩 Новая заявка\n\n"
        f"Имя: {data.get('name')}\n"
        f"Телефон: {data.get('phone')}\n"
        f"Комментарий: {data.get('comment')}"
    )

    for admin_id in ADMIN_IDS:
        await message.bot.send_message(admin_id, text)

    await message.answer("Заявка отправлена! Мы свяжемся с вами.")

    await state.clear()
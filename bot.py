from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
import asyncio

from config import BOT_TOKEN
from handlers import start, form, admin

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(start.router)
    dp.include_router(form.router)
    dp.include_router(admin.router)

    await bot.set_my_commands([
        BotCommand(command="start", description="Запуск"),
    ])

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
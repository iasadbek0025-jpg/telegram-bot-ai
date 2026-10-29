import asyncio
import logging
from aiogram import Bot, Dispatcher, F, html
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# BotFather'dan olgan tokeningizni quyidagi qo'shtirnoq ichiga yozing:
BOT_TOKEN = "8412628954:AAEsRn5Ha_0Rr7Ai3PKvSPGZlo0wCGgn594"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    reply_keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🤖 Bot haqida")]],
        resize_keyboard=True
    )
    await message.answer(
        f"Salom, {html.bold(message.from_user.full_name)}! 👋\n"
        f"Python 3.15 da yaratilgan botingiz muvaffaqiyatli ishlayapti!",
        reply_markup=reply_keyboard
    )

@dp.message(F.text == "🤖 Bot haqida")
async def about_handler(message: Message):
    await message.answer("Bu bot siz yaratgan ilk super Python 3.15 botidir! 🚀")

async def main():
    print("🚀 Bot muvaffaqiyatli ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
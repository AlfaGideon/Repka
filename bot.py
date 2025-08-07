
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
import asyncio
import os

API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'You bot token')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Кнопка для запуска Mini App
web_app_url = "https://your-miniapp-url.com"  # Замените на ваш URL
main_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Открыть мини-приложение', web_app=WebAppInfo(url=web_app_url))]],
    resize_keyboard=True
)


@dp.message(Command(commands=["start", "help"]))
async def send_welcome(message: types.Message):
    await message.reply(
        "Здравствуйте! Я бот-репетитор по русскому языку.\nВыберите действие:",
        reply_markup=main_kb
    )


@dp.message(Command(commands=["lesson"]))
async def lesson(message: types.Message):
    await message.reply("Сегодняшний урок: Правописание приставок.\nПример: пре- и при- ...")


@dp.message(Command(commands=["test"]))
async def test(message: types.Message):
    await message.reply("Тест: Выберите правильный вариант.\n1. Пр..красный (а) пре (б) при")


@dp.message(lambda message: message.text and 'мини-приложение' in message.text.lower())
async def open_miniapp(message: types.Message):
    await message.reply("Открываю мини-приложение...", reply_markup=main_kb)


if __name__ == '__main__':
    async def main():
        await dp.start_polling(bot)
    asyncio.run(main())

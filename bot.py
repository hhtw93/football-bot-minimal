import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# =================== КОНФИГ ===================
BOT_TOKEN = "7844584704:AAF6I6-SozsE7xJnrhbm4qWsoq6_huRn2jw"

# =================== ИНИЦИАЛИЗАЦИЯ ===================
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# =================== ЛОГИРОВАНИЕ ===================
logging.basicConfig(level=logging.INFO)

# =================== КОМАНДЫ ===================

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="📋 Все прогнозы")],
        [types.KeyboardButton(text="🎯 Экспресс дня")],
        [types.KeyboardButton(text="🏆 Топовые одиночные")],
        [types.KeyboardButton(text="📊 Статистика за день")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("📅 *ФУТБОЛЬНЫЕ ПРОГНОЗЫ*\nВыбери категорию:", reply_markup=keyboard, parse_mode="Markdown")

@dp.message(lambda message: message.text == "📋 Все прогнозы")
async def all_predictions(message: types.Message):
    await message.answer("*📋 ВСЕ ПРОГНОЗЫ НА СЕГОДНЯ*\n\n[Анализируем матчи...]\n\n*Ждите — данные загружаются.*", parse_mode="Markdown")

@dp.message(lambda message: message.text == "🎯 Экспресс дня")
async def express_day(message: types.Message):
    await message.answer("*🎯 ЭКСПРЕСС ДНЯ*\n\n[Подбираем самые надёжные исходы...]\n\n*Ждите — экспресс формируется.*", parse_mode="Markdown")

@dp.message(lambda message: message.text == "🏆 Топовые одиночные")
async def top_singles(message: types.Message):
    await message.answer("*🏆 ТОПОВЫЕ ОДИНОЧНЫЕ*\n\n[Выбираем самые проходимые ставки...]\n\n*Ждите — список готовится.*", parse_mode="Markdown")

@dp.message(lambda message: message.text == "📊 Статистика за день")
async def daily_stats(message: types.Message):
    await message.answer("*📊 СТАТИСТИКА ЗА ДЕНЬ*\n\n[Проверяем результаты матчей...]\n\n*Ждите — статистика обновляется.*", parse_mode="Markdown")

# =================== ЗАПУСК ===================

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, ADMIN_ID
from handlers import register_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
register_handlers(dp)

if __name__ == "__main__":
    print("Bot started...")
    executor.start_polling(dp, skip_updates=True)

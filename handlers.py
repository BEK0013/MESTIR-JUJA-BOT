from aiogram import types, Dispatcher
from menu import get_menu_text

async def start_handler(message: types.Message):
    menu_text = get_menu_text()
    await message.answer(menu_text, parse_mode="Markdown")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("🍗 Tovuq menyusi"))
    kb.add(KeyboardButton("📞 Admin bilan aloqa"))
    return kb

    

from aiogram import types, Dispatcher
from menu import get_menu_text

async def start_handler(message: types.Message):
    menu_text = get_menu_text()
    await message.answer(menu_text, parse_mode="Markdown")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
async def start_handler(message: types.Message):
        await message.answer("\u2705 Buyurtma berish uchun menyudan foydalaning", reply_markup=get_main_menu())

    @dp.message_handler(text="🍗 Tovuq menyusi")
    async def menu_handler(message: types.Message):
        await message.answer("1 dona qovurilgan tovuq - 50,000 so‘m\nKartoshka fri - 12,000 so‘m\nCola 0.5L - 5,000 so‘m")

    @dp.message_handler(text="📞 Admin bilan aloqa")
    async def contact_handler(message: types.Message):
        await message.answer("Admin bilan bog‘lanish: @BEK_DAMINOV\nTelefon: +998 95 772 99 93")

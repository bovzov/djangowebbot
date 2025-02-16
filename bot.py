from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils import executor

API_TOKEN = '7851164718:AAFTItRazQA-n0Zg0Gb0bLgiExCnSvfUNNU'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

cart_data = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    webapp_btn = InlineKeyboardButton(
        "Mahsulotlar", web_app=WebAppInfo(url="http://127.0.0.1:8000/")
    )
    cart_btn = InlineKeyboardButton("Savatni ko'rish", callback_data="show_cart")
    keyboard.add(webapp_btn, cart_btn)

    await message.answer("Mahsulotlar va savat menyusi:", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def webapp_data(message: types.Message):
    data = eval(message.web_app_data.data)
    cart_data[message.from_user.id] = data
    await message.answer("Savatga qo'shildi!")

@dp.callback_query_handler(lambda c: c.data == "show_cart")
async def show_cart(callback: types.CallbackQuery):
    user_cart = cart_data.get(callback.from_user.id, [])
    if not user_cart:
        await callback.answer("Savat bo'sh!")
    else:
        text = "\n".join([f"Mahsulot ID: {item['id']}, Soni: {item['count']}" for item in user_cart])
        await callback.message.answer(f"Savat:\n{text}")

executor.start_polling(dp)

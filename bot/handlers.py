from aiogram import types

cart = {}

def register_handlers(dp):
    dp.register_message_handler(start, commands="start")
    dp.register_message_handler(view_cart, commands="cart")
    dp.register_callback_query_handler(add_to_cart_callback, lambda c: c.data.startswith('add_to_cart'))

async def start(message: types.Message):
    await message.reply("Welcome to DPY Clothing Store! Use /cart to view your cart or click the buttons to add items.")

async def add_to_cart_callback(callback_query: types.CallbackQuery):
    item = callback_query.data.split(":")[1]
    cart[callback_query.from_user.id] = cart.get(callback_query.from_user.id, []) + [item]
    await callback_query.answer(f"Added {item} to your cart.")

async def view_cart(message: types.Message):
    items = cart.get(message.from_user.id, [])
    if items:
        await message.reply(f"Your cart: {', '.join(items)}. Total: {len(items)*1000} ₽. Use the web app to checkout.")
    else:
        await message.reply("Your cart is empty.")

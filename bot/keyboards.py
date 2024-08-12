from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_product_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton("Classic T-Shirt", callback_data="add_to_cart:tshirt"))
    keyboard.add(InlineKeyboardButton("Retro Jeans", callback_data="add_to_cart:jeans"))
    return keyboard

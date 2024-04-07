from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rasmlar"),
            KeyboardButton(text="Rasm Joylash")
        ]
    ], resize_keyboard=True
)


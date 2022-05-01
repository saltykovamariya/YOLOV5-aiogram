from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
format = ["Image"]
format_image = ["Detecting"]

buttons_image = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for i in format_image:
    buttons_image.add(KeyboardButton(i))


buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for i in format:
    buttons.add(KeyboardButton(i))

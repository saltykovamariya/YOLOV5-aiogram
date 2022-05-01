from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from my_bot.keyboards import buttons, buttons_image
import os


class Form(StatesGroup):
    choice_format = State()
    choice_text_type = State()
    choice_image_type = State()
    detect_image = State()

# @dp.message_handler(commands="start", state = "*")
async def start_def(message: types.Message):
    await Form.choice_format.set()
    await message.answer("hello!, what do you want?", reply_markup=buttons)

# @dp.message_handler(Text(equals="Image"), state=Form.choice_format)
async def image_def(message: types.Message, state = FSMContext):
    await Form.choice_image_type.set()
    await message.answer("Choice type of processing", reply_markup=buttons_image)

async def detect_image_def(message: types.Message, state = FSMContext):
    await Form.detect_image.set()
    await message.answer("Give me please a picture")

async def check_image_true_def(message: types.Message, state = FSMContext):
    # await message.answer("It's picture!")
    await message.photo[-1].download("my_bot/pictures/input.jpg",make_dirs=False)
    os.system("python yolov5/detect.py --weights yolov5/runs/train/exp2/weights/best.pt --source my_bot/pictures/input.jpg \
    --name /Users/masha/PycharmProjects/yolov5_telebot/my_bot/pictures/detect --exist-ok")
    await message.answer_photo(photo=open('my_bot/pictures/detect/input.jpg', 'rb'))


async def check_image_false_def(message: types.Message, state = FSMContext):
    await message.answer("Error")



def register_bot_handlers(dp: Dispatcher):
    dp.register_message_handler(start_def, commands="start", state = "*")
    dp.register_message_handler(image_def, Text(equals="Image"), state=Form.choice_format)
    dp.register_message_handler(detect_image_def,Text(equals="Detecting"), state=Form.choice_image_type)
    dp.register_message_handler(check_image_true_def, content_types=['photo'], state=Form.detect_image)
    dp.register_message_handler(check_image_false_def, state=Form.detect_image)
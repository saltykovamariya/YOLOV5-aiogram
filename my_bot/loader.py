from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token="5142128799:AAE9nKEovhW88FPMdVn57mFfTHNezONTX-Y", parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)
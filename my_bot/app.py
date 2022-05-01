from aiogram.utils import executor
from loader import dp
from my_bot.handlers import register_bot_handlers

register_bot_handlers(dp)
executor.start_polling(dp, skip_updates=True)
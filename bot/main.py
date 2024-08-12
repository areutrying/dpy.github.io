from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor

from handlers import register_handlers

TOKEN = '7030936713:AAGM4vll_M2w7TT1agBQtvOhtH4-GCtvf1g'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

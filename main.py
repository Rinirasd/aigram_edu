import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from app.handlers import router

bot = Bot(token='6183062996:AAFubx8HNGPZ0Eu0AgcKTM71KQfDu6knSis')
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
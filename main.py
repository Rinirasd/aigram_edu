import asyncio

from aiogram import Bot, Dispatcher,types,F
from aiogram.filters.command import Command

bot = Bot(token = '6183062996:AAFubx8HNGPZ0Eu0AgcKTM71KQfDu6knSis')
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message:types.Message)-> None:
    await message.answer("Привет это я ")


@dp.message(F.text)
async def message(message: types.Message)-> None:
    await message.answer("Ваше сообщение принято!")


async def main() :
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
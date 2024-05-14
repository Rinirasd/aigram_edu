import asyncio

from aiogram import Bot, types, F, Router
from aiogram.filters.command import Command
from aiogram.types import FSInputFile


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message)-> None:
    await message.answer("Привет это я ")


@router.message(Command("hello"))
async def hello(message: types.Message)-> None:
    await message.answer(f"{message.from_user}")



@router.message(F.text)
async def message(message: types.Message)-> None:
    await message.answer("Ваше сообщение принято!")



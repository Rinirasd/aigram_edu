import asyncio

from app.keyboards import start_keyboard, kb2, items
from aiogram import Bot, types, F, Router
from aiogram.filters.command import Command


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message)-> None:
    await message.reply("Привет это я ", reply_markup= start_keyboard)


@router.message(Command("hello"))
async def hello(message: types.Message)-> None:
    await message.answer(f"{message.from_user}")


@router.message(F.text == "Начать")
async def Go(message: types.Message)-> None:
    await message.answer("Здарово братан !")


@router.message(Command("shop"))
async def cmd_start(message: types.Message)-> None:
    await message.reply("Привет, что хочешь купить", reply_markup=items)


@router.callback_query(F.data == "item_laptop")
async def device(callback: types.CallbackQuery):
    await callback.answer("Вы выбрали ноутбук!", show_alert=True)


@router.callback_query(F.data == "item_headphones")
async def device(callback: types.CallbackQuery):
    await callback.answer("Вы выбрали наушники!", show_alert=True)


@router.callback_query(F.data == "item_phone")
async def device(callback: types.CallbackQuery):
    await callback.answer("Вы выбрали телефон!", show_alert=True)

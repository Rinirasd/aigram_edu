import asyncio

from app.keyboards import start_keyboard, kb2, items
from aiogram import Bot, types, F, Router
from aiogram.filters.command import Command
from app.states import Reg, Question
from aiogram.fsm.context import FSMContext
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


@router.callback_query(F.data.startswith("item_"))
async def device(callback: types.CallbackQuery):
    _, item = callback.data.split("_")

    await callback.answer(f"Вы выбрали {item}", show_alert=True)


@router.message(Command("reg"))
async def reg_first(message: types.Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Введите имя")


@router.message(Reg.name)
async def reg_second(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.surname)
    await message.answer("Введите фамилию")


@router.message(Reg.surname)
async def reg_third(message: types.Message, state: FSMContext):
    await state.update_data(surname=message.text)
    data = await state.get_data()
    await message.answer("Информация принята")
    await message.answer(f"Приятно познакомиться  {data['surname']} {data ['name']}")
    await state.clear()


@router.message(Command("Question"))
async def reg_first(message: types.Message, state: FSMContext):
    await state.set_state(Question.first)
    await message.answer("Первый вопрос сколько будет 2+2 ? ")


@router.message(Question.first)
async def reg_second(message: types.Message, state: FSMContext):
    await state.update_data(first=message.text)
    await state.set_state(Question.Second)
    await message.answer("Второй вопрос сколько будет корень из 7569 ?")


@router.message(Question.Second)
async def reg_second(message: types.Message, state: FSMContext):
    await state.update_data(Second=message.text)
    await state.set_state(Question.Third)
    await message.answer("Третий вопрос сколько будет 8+8 ?")


@router.message(Question.Third)
async def reg_third(message: types.Message, state: FSMContext):
    await state.update_data(surname=message.text)
    data = await state.get_data()
    await message.answer("Информация принята")
    await message.answer(f"Приятно познакомиться  {data['surname']} {data ['name']}")
    await state.clear()


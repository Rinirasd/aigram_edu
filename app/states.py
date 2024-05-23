from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


class Reg(StatesGroup):
    name = State()
    surname = State()

class Question(StatesGroup):
    first = State()
    Second = State()
    Third = State()
    Fourth = State()

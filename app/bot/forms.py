from aiogram.fsm.state import StatesGroup, State


class Registration(StatesGroup):
    key = State()


class AskQuestion(StatesGroup):
    answer = State()
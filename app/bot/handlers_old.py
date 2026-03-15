import app.bot.keyboards as kb

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from app.bot.middlewares import TestMiddleware

router = Router()

router.message.outer_middleware(TestMiddleware())
router.message.filter(F.chat.type == "private")


class Registration(StatesGroup):
    name = State()
    number = State()


# Файл utils.py или как-нибудь так, или в пакет БД положу, хз:
# ============================== #

def get_servers():
    return ['NL', 'FR', 'DE', 'RU', 'FI']

# ============================== #


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Привет, я нейроаболтус, который поможет тебе сориентироваться в дебрях БФУ им. И. Канта. Я умею:\n" +
                        f"- Перенапрявлять тебя к наставникам\n" +
                        f"- Перенаправлять тебя в МФЦ\n" +
                        f"- Периодически давать полезную информацию", reply_markup=kb.lets_start)


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer("Ща хелпану погодь")


@router.message(F.text == "Как дела?")
async def whats_up(message: Message):
    await message.answer("Ваще с кайфом")


@router.message(F.photo)
async def whats_up(message: Message):
    await message.answer(f"ID фото: {message.photo[-1].file_id}")


@router.callback_query(F.data.in_(get_servers()))
async def country(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f"Ты выбрал сервер {callback.data}.\nТвои действия?", reply_markup=kb.server_settings)


# РЕГИСТРАЦИЯ

@router.message(Command("reg"))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer('Введите ваше имя')


@router.message(Registration.name) 
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Registration.number)
    await message.answer('Введите номер телефона')


@router.message(Registration.number) 
async def reg_three(message: Message, state: FSMContext):
    await state.update_data(number = message.text)
    data = await state.get_data()
    await message.answer(f'ТЫ СПРАВИЛСЯ !!!\n{data['name']} {data['number']}')
    await state.clear()
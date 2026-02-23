import keyboards as kb

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from middlewares import TestMiddleware
from config import Config
from forms import Registration


router = Router()


@router.callback_query()
async def insert_key(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Registration.key)
    await callback.answer()
    await callback.message.edit_text("Бот пока что находится в закрытой бете, так что необходимо ввести ключ:")


@router.message(Registration.key)
async def auth(message: Message, state: FSMContext):
    if message.text == Config.access_key:
        await message.answer("Откуда ты его знаешь? -_-", reply_markup=kb.user)
        await state.update_data(key = message.text)
        await state.clear()
    else:
        await message.answer("Попался за руку как дешевка. Давай еще раз")
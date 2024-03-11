from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.prof_keyboards import make_row_keyboard



router = Router()


available_sex = ["Мальчик", "Девочка", "Иностранец"]
available_age = ["до 18", "от 18 до 90", "90+"]


class ChoiceSexAge(StatesGroup):
    choice_sex = State()
    choice_age = State()


#Хэндлер на команду /anketa
@router.message(Command('anketa'))
async def cmd_prof(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(
    f'Привет, {name}, заполни анкету! Укажи пол!',
    reply_markup=make_row_keyboard(available_sex)
    )
    await state.set_state(ChoiceSexAge.choice_sex)


@router.message(ChoiceSexAge.choice_sex, F.text.in_(available_sex))
async def prof_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_sex=message.text.lower())
    await message.answer(
    text='Спасибо, Укажи диапазон возраста',
    reply_markup=make_row_keyboard(available_age)
    )
    await state.set_state(ChoiceSexAge.choice_age)


@router.message(ChoiceSexAge.choice_sex)
async def prof_chosen_incorrectly(message: types.Message):
    await message.answer(
    'Я не знаю такого пола',
    reply_markup=make_row_keyboard(available_sex)
    )


@router.message(ChoiceSexAge.choice_age, F.text.in_(available_age))
async def grade_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
    f'Ваш возраст {message.text.lower()}. Ваш пол {user_data.get("chosen_sex")}',
    reply_markup=types.ReplyKeyboardRemove()
    )
    await state.clear()


@router.message(ChoiceSexAge.choice_age)
async def grade_chosen_incorrectly(message: types.Message):
    await message.answer(
    'Я не знаю такого возраста',
    reply_markup=make_row_keyboard(available_age)
    )
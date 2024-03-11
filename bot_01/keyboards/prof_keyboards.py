from aiogram import types


def make_row_keyboard(items: list[str]) -> types.ReplyKeyboardMarkup:
    row = [types.KeyboardButton(text=item) for item in items]
    return types.ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)

def make_row_keyboard2(items: list[str]) -> types.ReplyKeyboardMarkup:
    #row = [types.KeyboardButton(text=item) for item in items]
    row = [types.KeyboardButton(text='1'),types.KeyboardButton(text='2'),types.KeyboardButton(text='3'),
           types.KeyboardButton(text='4'), types.KeyboardButton(text='5'), types.KeyboardButton(text='6'),
           types.KeyboardButton(text='7'), types.KeyboardButton(text='8'), types.KeyboardButton(text='9')]

    return types.ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
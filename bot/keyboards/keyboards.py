from aiogram import types


async def create_keyboard_for_task_type(task_id):
    type_keyboard = types.InlineKeyboardMarkup(row_width=1)
    inline_btn_1 = types.InlineKeyboardButton('Баг/Ошибка', callback_data='bug_{}'.format(task_id))
    inline_btn_2 = types.InlineKeyboardButton('Доработка', callback_data='feat_{}'.format(task_id))
    type_keyboard.add(inline_btn_1, inline_btn_2)
    return type_keyboard


async def create_keyboard_for_task_status(task_id):
    status_keyboard = types.InlineKeyboardMarkup(row_width=1)
    inline_btn_1 = types.InlineKeyboardButton('Принято', callback_data='sel_{}'.format(task_id))
    inline_btn_2 = types.InlineKeyboardButton('Отклонено', callback_data='rej_{}'.format(task_id))
    status_keyboard.add(inline_btn_1, inline_btn_2)
    return status_keyboard


async def create_keyboard_for_task_reject(task_id):
    reject_keyboard = types.InlineKeyboardMarkup(row_width=1)
    inline_btn_1 = types.InlineKeyboardButton('Слишком плохо описан запрос', callback_data='TR_nei_{}'.format(task_id))
    inline_btn_2 = types.InlineKeyboardButton('Такого больше не может повторится', callback_data='TR_cbr_{}'.format(task_id))
    inline_btn_3 = types.InlineKeyboardButton('Уже в работе', callback_data='TR_aiw_{}'.format(task_id))
    reject_keyboard.add(inline_btn_1, inline_btn_2, inline_btn_3)
    return reject_keyboard
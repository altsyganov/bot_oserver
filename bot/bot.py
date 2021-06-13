import aiohttp
from aiogram import executor, types
from aiogram.dispatcher.filters import Text

from config.config import ping_name
from utils.api import API
from utils.utils import reject_text
from keyboards.keyboards import create_keyboard_for_task_status, create_keyboard_for_task_type, create_keyboard_for_task_reject

from loader import dp, bot

session = aiohttp.ClientSession()
api = API(session=session)


@dp.message_handler(lambda message: all((ping_name in message.text, message.text.replace(ping_name, ''))))
async def ping(message):
    bot_dict = await api.retrieve_bot(ping_name=ping_name)
    print(message.chat)
    print(dir(message))
    text = message.text.replace(ping_name, '')
    print(text)
    # Здесь нужен какой-то фильтр
    if message.chat['id'] != -591262988:
        if len(text) < 10:
            await message.reply('Подозрительно маленькая формулировка задачи/бага')
        else:
            clients = await api.list_clients()
            print(clients)
            for client in clients:
                if client['chat_id'] == message.chat['id']:
                    task = await api.create_request(payload={'client': message.chat['id'], 'body': text,
                                                             'message_id': message.message_id})
                    keyboard = await create_keyboard_for_task_status(task['id'])
                    await bot.send_message(chat_id=bot_dict['parent_chat_id'], reply_markup=keyboard, text=task)
            await message.reply('Отправлено к разработчикам')


@dp.callback_query_handler(lambda callback_query: 'rej' in callback_query.data)
async def process_rejected(query):
    bot_dict = await api.retrieve_bot(ping_name=ping_name)
    print(query.data.rsplit('_'))
    action, task_id = query.data.rsplit('_')
    reject_keyboard = await create_keyboard_for_task_reject(task_id=task_id)
    await bot.edit_message_text(chat_id=bot_dict['parent_chat_id'], message_id=query.message.message_id,
                                text='Отказались от задачи', reply_markup=reject_keyboard)


@dp.callback_query_handler(lambda callback_query: 'sel' in callback_query.data)
async def process_selected(query):
    bot_dict = await api.retrieve_bot(ping_name=ping_name)
    print(query.data.rsplit('_'))
    action, task_id = query.data.rsplit('_')
    payload = {
        'status': action
    }
    response = await api.update_request(task_id=task_id, payload=payload)
    if action == 'sel':
        await bot.send_message(chat_id=response['client'], text='Принято', reply_to_message_id=response['message_id'])
        type_keyboard = await create_keyboard_for_task_type(task_id=task_id)
        await bot.edit_message_text(chat_id=bot_dict['parent_chat_id'], message_id=query.message.message_id,
                                    text='Выберите тип для данного запроса', reply_markup=type_keyboard)


@dp.callback_query_handler(lambda callback_query: any(('bug' in callback_query.data, 'feat' in callback_query.data)))
async def process_type(query):
    bot_dict = await api.retrieve_bot(ping_name=ping_name)
    print(query.message.chat)
    type, task_id = query.data.rsplit('_')
    payload = {
        'type': type
    }
    response = await api.update_request(task_id=task_id, payload=payload)
    await bot.edit_message_text(chat_id=bot_dict['parent_chat_id'], message_id=query.message.message_id,
                                text='{}\n\nВыбран тип {}.\n\n{}'.format(bot_dict['{}_responsible'.format(type)], type, response), reply_markup=None)


@dp.callback_query_handler(lambda callback_query: 'TR' in callback_query.data)
async def process_reject(query):
    bot_dict = await api.retrieve_bot(ping_name=ping_name)
    print(query.message.chat)
    _, type, task_id = query.data.rsplit('_')
    payload = {
        'status': 'rej'
    }
    response = await api.update_request(task_id=task_id, payload=payload)
    await bot.send_message(chat_id=response['client'], text='Отклонено по причине: {}'.format(reject_text[type]),
                           reply_to_message_id=response['message_id'])
    await bot.edit_message_text(chat_id=bot_dict['parent_chat_id'], message_id=query.message.message_id,
                                text='{}\n\nОтклонено по причине: {}'.format(response, reject_text[type]), reply_markup=None)


if __name__ == '__main__':
    executor.start_polling(dp)

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from buttons import user_kb, user_kb_inline_kb
import datetime
import os

bot = Bot('5846191784:AAHRbeVwS5SfmfzgSI0gFDNbOCrushXr6S8')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, я бот :)', reply_markup=user_kb)
    await message.answer('Можешь узнать дату?', reply_markup=user_kb_inline_kb)


@dp.message_handler(Text(equals='Пожелание доброго утра', ignore_case=True))
async def good_morning(message: types.Message):
    await message.answer('Доброе утро!')


@dp.message_handler(Text(equals='Пожелание доброй ночи', ignore_case=True))
async def night_morning(message: types.Message):
    await message.answer('Доброй ночи!')


@dp.callback_query_handler(text='button_date')
async def date(callback_query: types.CallbackQuery):

    date_now = datetime.datetime.now()
    message = date_now.strftime('%d-%m-%Y %H:%M:%S')
    await bot.send_message(callback_query.from_user.id, message)

    await bot.answer_callback_query(callback_query.id)

if __name__ == '__main__':
    print('bot polling started')
    executor.start_polling(dp, skip_updates=True)


# , 'Привет, я всё сделал', show_alert=True
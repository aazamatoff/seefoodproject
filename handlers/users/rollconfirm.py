from aiogram import types
from aiogram.utils import callback_data
from handlers.users.start import g
from keyboards.default.desert import desert
from loader import dp, bot


@dp.callback_query_handler(text=['buy9'])
async def lesafsafssazs(call: types.CallbackQuery):
    g.append('Roll')
    await call.message.answer("✅ Successfully added!", reply_markup=desert)


@dp.callback_query_handler(text=['dont9'])
async def sasdasdf(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Choose what you would like to", reply_markup=desert)
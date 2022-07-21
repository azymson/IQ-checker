from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp 
a = 0

@dp.message_handler(Text(contains = "+",  ignore_case=True))
async def russiann_bad_words(msg: types.Message):
    
    await msg.reply("fsda")


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


post_callback = CallbackData("create_post", "action")

key1 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Parij", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="London", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="Nyu-York", callback_data="True"),
    ],
    [
        InlineKeyboardButton(text="Tokio", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="Pekin", callback_data="False"),
    ],
])

key2= InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Juma", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="Shanba", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="Yakshanba", callback_data="True"),
    ],
    [
        InlineKeyboardButton(text="Dushanba", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="Seshanba", callback_data="False"),
    ],
])

key3 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="48", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="64", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="72", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="66", callback_data="True"),
    ],
    [
        InlineKeyboardButton(text="68", callback_data="False"),
    ],
])

key4 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="3", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="4", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="4 1/2", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="5", callback_data="True"),
    ],
    [
        InlineKeyboardButton(text="6", callback_data="False"),
    ],
])

key5 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Missiya", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="Xavfli", callback_data="True"),
    ],
    [
        InlineKeyboardButton(text="Bajarildi", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="To'xtating", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="Muvaffaqiyatli", callback_data="False"),
    ],
])

key6 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="44", callback_data="True"),
    ],
    [
        InlineKeyboardButton(text="50", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="42", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="40", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="46", callback_data="False"),
    ],
])

key7 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="U mening Akam", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="U mening Amakim", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="U mening Otam", callback_data="True"),
    ],
    [
        InlineKeyboardButton(text="U mening Singlim", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="U menga begona", callback_data="False"),
    ],
])

key8 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="11", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="15", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="5", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="4", callback_data="True"),
    ],
    [
        InlineKeyboardButton(text="7", callback_data="False"),
    ],
])

key9 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="3", callback_data="True"),
    ],
    [
        InlineKeyboardButton(text="4", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="1", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="2", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="6", callback_data="False"),
    ],
])

key10 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Rost", callback_data="True"),
    ],
    [
        InlineKeyboardButton(text="Yolg'on", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="Aniqlab bo'lmaydi", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="To'risini aytsam farqiga bormayman", callback_data="False"),
    ],
    [
        InlineKeyboardButton(text="Juda qiyin savolku", callback_data="False"),
    ],
])

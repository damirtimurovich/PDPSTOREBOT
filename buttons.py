from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

key = [
    [KeyboardButton(text="🇺🇿 O'zbekcha"), KeyboardButton(text="🇷🇺 Русский")],
    [KeyboardButton(text="🇺🇸 English")]
]
keyboard = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)


##################### #uzbek

sezon = [
    [types.KeyboardButton(text="👨‍💻Back-end"), types.KeyboardButton(text="👨‍💻Front-end")],
    [types.KeyboardButton(text="⬅ orqaga")]
]
sezonkey = types.ReplyKeyboardMarkup(keyboard=sezon, resize_keyboard=True)

###################### #uzbek

keyWen = [
    [types.KeyboardButton(text="Pyhton -uz"), types.KeyboardButton(text="Django -uz")],
    [types.KeyboardButton(text="Java -uz "),types.KeyboardButton(text="Php -uz")],
    [types.KeyboardButton(text="C# -uz"), types.KeyboardButton(text="C++ -uz")],
    [types.KeyboardButton(text="SQLite -uz")],
    [types.KeyboardButton(text="⬅orqaga")]
]

wenKey = types.ReplyKeyboardMarkup(keyboard=keyWen, resize_keyboard=True)

####################### #rus

russss = [
    [types.KeyboardButton(text="Pyhton -ru "), types.KeyboardButton(text="Django -ru")],
    [types.KeyboardButton(text="Java -ru "),types.KeyboardButton(text="Php -ru ")],
    [types.KeyboardButton(text="C# -ru "), types.KeyboardButton(text="C++ -ru ")],
    [types.KeyboardButton(text="SQLite -ru ")],
    [types.KeyboardButton(text="⬅Назад")]
]

russ = types.ReplyKeyboardMarkup(keyboard=russss, resize_keyboard=True)

###################### #rus

russdf = [
    [types.KeyboardButton(text="👨‍💻Back end"), types.KeyboardButton(text="👨‍💻Front end")],
    [types.KeyboardButton(text="⬅ Назад")]
]

russvgb = types.ReplyKeyboardMarkup(keyboard=russdf, resize_keyboard=True)


############################## #rus

russd = [
    [types.KeyboardButton(text="HTML -ru"), types.KeyboardButton(text="CSS -ru")],
    [types.KeyboardButton(text="JavaScript -ru"),types.KeyboardButton(text="ReactJS -ru")],
    [types.KeyboardButton(text="⬅Назад")]
]

rusddf = types.ReplyKeyboardMarkup(keyboard=russd, resize_keyboard=True)


##################################### #uzbek

frogt = [
    [types.KeyboardButton(text="HTML -uz"), types.KeyboardButton(text="CSS -uz")],
    [types.KeyboardButton(text="JavaScript -uz"),types.KeyboardButton(text="ReactJS -uz")],
    [types.KeyboardButton(text="⬅orqaga")]
]

frogtg = types.ReplyKeyboardMarkup(keyboard=frogt, resize_keyboard=True)

################################ #english

english = [
    [types.KeyboardButton(text="HTML -en"), types.KeyboardButton(text="CSS -en")],
[types.KeyboardButton(text="JavaScript -en"),types.KeyboardButton(text="ReactJS -en")],
    [types.KeyboardButton(text="⬅back")]
]

englishsh = types.ReplyKeyboardMarkup(keyboard=english, resize_keyboard=True)

############################### #english

english2 = [
    [types.KeyboardButton(text="👨‍💻Backend"), types.KeyboardButton(text="👨‍💻Frontend")],
    [types.KeyboardButton(text="⬅ back")]
]

englishsh2 = types.ReplyKeyboardMarkup(keyboard=english2, resize_keyboard=True)

############################## #enlish

english3 = [
    [types.KeyboardButton(text="Pyhton -en"), types.KeyboardButton(text="Django -en")],
    [types.KeyboardButton(text="Java -en"),types.KeyboardButton(text="Php -en")],
    [types.KeyboardButton(text="C# -en"), types.KeyboardButton(text="C++ -en")],
    [types.KeyboardButton(text="SQLite -en")],
    [types.KeyboardButton(text="⬅back")]
]

englishsh3 = types.ReplyKeyboardMarkup(keyboard=english3, resize_keyboard=True)

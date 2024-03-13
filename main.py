import asyncio
import time
import logging
import sys
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from root import TOKEN
from func import start_upp, shut_downn
from buttons import keyboard, sezonkey, wenKey, russ, russvgb, rusddf, frogtg, englishsh, englishsh2, englishsh3
from shopkey import pythonuz, pythonru, pythonen, javauz, javaru, javaen, cuz, cru, cen, phpuz, phpru, phpen, djangouz, \
    djangoru, djangoen, JavaScriptuz, JavaScriptru, JavaScripten, ccuz, ccru, ccen, sqlliteuz, sqlliteru, sqlliteen, \
    HTMLen, HTMLru, HTMLuz, cssuz, cssru, cssen, ReactJSuz, ReactJSru, ReactJSen

from aiogram.utils.keyboard import InlineKeyboardBuilder
from db import Database

db = Database("users.db")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    db.add_user(message.from_user.id, message.from_user.full_name)
    await message.answer("🇺🇿-Tilni tanlang \n🇷🇺-Выберите язык \n🇺🇸-Select a language", reply_markup=keyboard)


@dp.message(Command("www"))
async def all_users(message: Message):
    db.get_all_users()
    for user in db.get_all_users():
        await message.answer(f"UserId: {user[0]}, FullName: {user[1]}")


#################################### #start


#################################### #start
# ------------------>>>>>
#################################### #rus
@dp.message(F.text == "⬅Назад")
async def froty(message: Message):
    await message.answer("Выберите язык", reply_markup=russvgb)


@dp.message(F.text == "👨‍💻Back end")
async def frot(message: Message):
    await message.answer("Back-end страница", reply_markup=russ)


@dp.message(F.text == "👨‍💻Front end")
async def front(message: Message):
    await message.answer("Front-end страница", reply_markup=rusddf)


@dp.message(F.text == "🇷🇺 Русский")
async def keyimlar(message: Message):
    await message.answer("Выберите  язык программирования!", reply_markup=russvgb)


@dp.message(F.text == "⬅ Назад")
async def keyimmlar(message: Message):
    await message.answer("🇺🇿-Tilni tanlang \n🇷🇺-Выберите язык \n🇺🇸-Select a language", reply_markup=keyboard)


#################################### #rus
# ------------------>>>>>
#################################### #uzbek
@dp.message(F.text == "🇺🇿 O'zbekcha")
async def keyimlar(message: Message):
    await message.answer("Dasturlash tilini tanlang!", reply_markup=sezonkey)


@dp.message(F.text == "👨‍💻Back-end")
async def keyimlar(message: Message):
    await message.answer("Back-end sahifasi", reply_markup=wenKey)


@dp.message(F.text == "👨‍💻Front-end")
async def keyar(message: Message):
    await message.answer("Front-end sahifasi", reply_markup=frogtg)


@dp.message(F.text == "⬅orqaga")
async def keyimlar(message: Message):
    await message.answer("Dasturlash tilini tanlang!", reply_markup=sezonkey)


@dp.message(F.text == "⬅ orqaga")
async def kyimlar(message: Message):
    await message.answer("🇺🇿-Tilni tanlang \n🇷🇺-Выберите язык \n🇺🇸-Select a language", reply_markup=keyboard)


#################################### #uzbek
# ------------------>>>>>
#################################### #english
@dp.message(F.text == "🇺🇸 English")
async def english1(message: Message):
    await message.answer("Choose  programming language!", reply_markup=englishsh2)


@dp.message(F.text == "👨‍💻Backend")
async def english2(message: Message):
    await message.answer("Back-end page", reply_markup=englishsh3)


@dp.message(F.text == "👨‍💻Frontend")
async def english3(message: Message):
    await message.answer("Front-end page", reply_markup=englishsh)


@dp.message(F.text == "⬅back")
async def english4(message: Message):
    await message.answer("Choose your programming language!", reply_markup=englishsh2)


@dp.message(F.text == "⬅ back")
async def english4(message: Message):
    await message.answer("🇺🇿-Tilni tanlang \n🇷🇺-Выберите язык \n🇺🇸-Select a language", reply_markup=keyboard)

    #################################### #english
    # ------------------>>>>>

    '''Back-end'''


#################################### #python
@dp.message(F.text == "Pyhton -uz")
async def shop(message: Message):
    await message.answer("Tanlang ⬇",
                         reply_markup=pythonuz.as_markup())


@dp.message(F.text == "Pyhton -ru")
async def shop(message: Message):
    await message.answer("Выберите ⬇",
                         reply_markup=pythonru.as_markup())


@dp.message(F.text == "Pyhton -en")
async def shop(message: Message):
    await message.answer("Select ⬇",
                         reply_markup=pythonen.as_markup())


#################################### #python
# ------------------>>>>>
#################################### #java
@dp.message(F.text == "Java -uz")
async def shop(message: Message):
    await message.answer("Tanlang ⬇",
                         reply_markup=javauz.as_markup())


@dp.message(F.text == "Java -ru")
async def shop(message: Message):
    await message.answer("Выберите ⬇",
                         reply_markup=javaru.as_markup())


@dp.message(F.text == "Java -en")
async def shop(message: Message):
    await message.answer("Select ⬇ ",
                         reply_markup=javaen.as_markup())


################################## #java
# ------------------>>>>>
################################## #C#
@dp.message(F.text == "C# -uz")
async def shop(message: Message):
    await message.answer("Tanlang ⬇ ",
                         reply_markup=cuz.as_markup())


@dp.message(F.text == "C# -ru")
async def shop(message: Message):
    await message.answer("Выберите ⬇ ",
                         reply_markup=cru.as_markup())


@dp.message(F.text == "C# -en")
async def shop(message: Message):
    await message.answer("Select ⬇ ",
                         reply_markup=cen.as_markup())


################################## #C#
# ------------------>>>>>
################################## #Php
@dp.message(F.text == "Php -uz")
async def shop(message: Message):
    await message.answer("Tanlang ⬇",
                         reply_markup=phpuz.as_markup())


@dp.message(F.text == "Php -ru")
async def shop(message: Message):
    await message.answer("Выберите ⬇",
                         reply_markup=phpru.as_markup())


@dp.message(F.text == "Php -en")
async def shop(message: Message):
    await message.answer("Select ⬇",
                         reply_markup=phpen.as_markup())


################################## #Php
# ------------------>>>>>
################################## #Django
@dp.message(F.text == "Django -uz")
async def shop(message: Message):
    await message.answer("Tanlang ⬇",
                         reply_markup=djangouz.as_markup())


@dp.message(F.text == "Django -ru")
async def shop(message: Message):
    await message.answer("Выберите ⬇ ",
                         reply_markup=djangoru.as_markup())


@dp.message(F.text == "Django -en")
async def shop(message: Message):
    await message.answer("Select ⬇ ",
                         reply_markup=djangoen.as_markup())


################################## #Django
# ------------------>>>>>
# ------------------>>>>>
################################ #C/C++
@dp.message(F.text == "C++ -uz")
async def shop(message: Message):
    await message.answer("Tanlang ⬇",
                         reply_markup=ccuz.as_markup())


@dp.message(F.text == "C++ -ru")
async def shop(message: Message):
    await message.answer("Выберите ⬇",
                         reply_markup=ccru.as_markup())


@dp.message(F.text == "C++ -en")
async def shop(message: Message):
    await message.answer("Select ⬇",
                         reply_markup=ccen.as_markup())


################################ #C/C++
# ------------------>>>>>
################################ #Sql lite
@dp.message(F.text == "SQLite -uz")
async def shop(message: Message):
    await message.answer("Tanlang ⬇",
                         reply_markup=sqlliteuz.as_markup())


@dp.message(F.text == "SQLite -ru")
async def shop(message: Message):
    await message.answer("Выберите ⬇",
                         reply_markup=sqlliteru.as_markup())


@dp.message(F.text == "SQLite -en")
async def shop(message: Message):
    await message.answer("Select ⬇ ",
                         reply_markup=sqlliteen.as_markup())
    ################################ #Sql lite
    # ------------------>>>>>

    '''Front-end'''


#################################### #html
@dp.message(F.text == "HTML -uz")
async def shop(message: Message):
    await message.answer("Tanlang ⬇ ",
                         reply_markup=HTMLuz.as_markup())


@dp.message(F.text == "HTML -ru")
async def shop(message: Message):
    await message.answer("Выберите ⬇",
                         reply_markup=HTMLru.as_markup())


@dp.message(F.text == "HTML -en")
async def shop(message: Message):
    await message.answer("Select ⬇ ",
                         reply_markup=HTMLen.as_markup())


#################################### #html
# ------------------>>>>>
#################################### #CSS
@dp.message(F.text == "CSS -uz")
async def shop(message: Message):
    await message.answer("Tanlang ⬇ ",
                         reply_markup=cssuz.as_markup())


@dp.message(F.text == "CSS -ru")
async def shop(message: Message):
    await message.answer("Выберите ⬇ ",
                         reply_markup=cssru.as_markup())


@dp.message(F.text == "CSS -en")
async def shop(message: Message):
    await message.answer("Select ⬇ ",
                         reply_markup=cssen.as_markup())


#################################### #CSS
# ------------------>>>>>
################################## #JavaScript
@dp.message(F.text == "JavaScript -uz")
async def shop(message: Message):
    await message.answer("Tanlang ⬇",
                         reply_markup=JavaScriptuz.as_markup())


@dp.message(F.text == "JavaScript -ru")
async def shop(message: Message):
    await message.answer("Выберите ⬇",
                         reply_markup=JavaScriptru.as_markup())


@dp.message(F.text == "JavaScript -en")
async def shop(message: Message):
    await message.answer("Select ⬇",
                         reply_markup=JavaScripten.as_markup())


################################## #JavaScript
# ------------------>>>>>
################################## #ReactJS
@dp.message(F.text == "ReactJS -uz")
async def shop(message: Message):
    await message.answer("Tanlang ⬇",
                         reply_markup=ReactJSuz.as_markup())


@dp.message(F.text == "ReactJS -ru")
async def shop(message: Message):
    await message.answer("Выберите ⬇",
                         reply_markup=ReactJSru.as_markup())


@dp.message(F.text == "ReactJS -en")
async def shop(message: Message):
    await message.answer("Select ⬇",
                         reply_markup=ReactJSen.as_markup())


################################## #ReactJS


#################################### #help
@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("""🇺🇺🇿 O'zbekcha

Bizning botimiz sizga IT yo`nalishidagi dasturlash tillari haqida foydali ma`lumotlar va linklar topib bera oladi. 

________________________________

🇷🇷🇺 Русский

Наш бот расскажет вам о языках программирования по направлению IT можете найти полезную информацию и ссылки.

________________________________

🇺🇺🇸 English

Our bot tells you about programming languages in the IT direction can find useful information and links.

""")


#################################### #helpda

@dp.message(Command("admin"))
async def contact(message: types.Message):
    f = "Saidxoja Developer"
    await message.answer_contact('+998903373550', first_name=f)
    s = "Damir"
    await message.answer_contact('+998334565959', first_name=s)


#################################### #community
@dp.message(Command("community"))
async def help(message: Message):
    await message.answer("https://t.me/pdpcommunity1")


#################################### #community


async def main() -> None:
    dp.startup.register(start_upp)
    dp.shutdown.register(shut_downn)
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

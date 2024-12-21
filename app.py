import asyncio
import logging
import config
import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from user import User

class App:
    __bot: Bot
    __dp: Dispatcher

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.__bot = Bot(token=config.token)
        self.__dp = Dispatcher()
        self.__handlers()

    def __handlers(self):
        # TODO: сделать нормальную регистрацию и добавление в бд
        @self.__dp.message(Command("start"))
        async def cmd_start(message: types.Message):
            user = User(message.from_user.id)
            logging.info(f"User {user} started the bot")
            await message.answer("Hello!")

        @self.__dp.message(Command("help"))
        async def cmd_help(message: types.Message):
            user = User(message.from_user.id)
            logging.info(f"User {user} need help from bot")
            await message.answer("Help!")

        @self.__dp.message()
        async def echo(message: types.Message):
            user = User(message.from_user.id)
            logging.info(f"User {user} send echo message: {message.text}")
            await message.answer(message.text)

    async def main(self):
        await self.__dp.start_polling(self.__bot)

    def run(self):
        asyncio.run(self.main())
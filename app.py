import asyncio
import logging
import config

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from user import User

class App:
    __bot: Bot
    __dp: Dispatcher
    __handler_register: dict

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        # TODO: создать конфиг и перенести все важные данные в него
        self.__bot = Bot(token=config.token)
        self.__dp = Dispatcher()
        self.__register_handlers()

    def __register_handlers(self):
        # TODO: сделать нормальную регистрацию и добавление её в базу данных
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

        @self.__dp.message(Command("help"))
        async def echo(message: types.Message):
            user = User(message.from_user.id)
            logging.info(f"User {user} need help from bot")
            await message.answer("Help!")

    async def main(self):
        await self.__dp.start_polling(self.__bot)

    def run(self):
        asyncio.run(self.main())
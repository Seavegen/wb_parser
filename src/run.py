""" Исполняемый файл
"""
import asyncio
import logging
import os
from aiogram.utils import executor
from aiogram.types import Message

from loader import dp, bot
from src.login_to_wb import auth_to_wb
from state import CaptchaAndPhoneState


@dp.message_handler(commands='start')
async def start(message: Message):

    if not os.path.exists('captcha_img'):
        os.mkdir('captcha_img')

    if not os.path.isfile('captcha_img'):
        auth_to_wb()

    await bot.send_photo(
        message.chat.id,
        photo=open('captcha_img/captcha.png', 'rb')
    )
    await message.answer('Введите каптчу:')
    await CaptchaAndPhoneState.captcha.set()


async def on_startup():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook()


# def main() -> None:
    # parsing_to_selenium(driver)
    # me = [parsing_to_selenium(driver)]
    # asyncio.gather(*me)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(parsing_to_selenium(driver))
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)

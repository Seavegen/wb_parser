import os
import urllib
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.by import By
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from config import login
from loader import dp, bot
from services import delay, user_agent
from state import CaptchaAndPhoneState


ua = user_agent()
option = webdriver.ChromeOptions()
option.add_argument("--disable-blink-features=AutomationControlled")
option.add_argument('--disable-notifications')
option.add_argument(f'--user-agent={ua}')
driver = webdriver.Chrome(os.getcwd() + "/chromedriver", options=option)


def auth_to_wb():
    """ Логиниться на wildberries
    """
    try:
        driver.get("https://www.wildberries.ru/security/login")
        driver.find_element(By.CLASS_NAME, 'input-item').send_keys(login)
        delay()
        driver.find_element(By.ID, 'requestCode').click()
        delay()
        img = driver.find_element(By.CLASS_NAME, 'captcha-image')
        src = img.get_attribute('src')
        urllib.request.urlretrieve(src, "captcha_img/captcha.png")
    except Exception as e:
        print(e)


@dp.message_handler(state=CaptchaAndPhoneState.captcha)
async def set_captcha(message: Message, state: FSMContext):
    captcha = message.text
    driver.find_element(By.ID, 'smsCaptchaCode').send_keys(captcha)
    delay()
    driver.find_element(By.CLASS_NAME, 'c-btn-main-lg-v1').click()
    delay()
    await message.answer('Каптча отправлена !')
    await message.answer('Введите код из СМС !')
    await CaptchaAndPhoneState.phone.set()


@dp.message_handler(state=CaptchaAndPhoneState.phone)
async def get_sms_code_phone(message: Message, state: FSMContext):
    sms_code_phone = message.text
    driver.find_element(By.CLASS_NAME, 'j-input-confirm-code').send_keys(sms_code_phone)
    delay()
    driver.find_element(By.ID, 'requestCode').click()
    delay()
    await message.answer('Вы успешно авторизовались!')
    await state.finish()

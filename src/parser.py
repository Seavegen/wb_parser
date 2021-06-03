""" Парсинг
"""
from selenium import webdriver
from services import delay, user_agent
from config import login
import pickle
import os


ua = user_agent()
option = webdriver.ChromeOptions()
option.add_argument("--disable-blink-features=AutomationControlled")
option.add_argument('--disable-notifications')
option.add_argument(f'--user-agent={ua}')
option.add_argument('--disable-extensions')
option.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(os.getcwd() + "/chromedriver", options=option)


def wb_parser():
    try:
        driver.get('https://www.wildberries.ru')
        for cookie in pickle.load(open(f"{login}_cookies", "rb")):
            driver.add_cookie(cookie)
        delay()
        driver.refresh()
        delay()
    except Exception as error:
        print(error)

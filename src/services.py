""" Сервисы
"""
import os
import random
import time
from selenium import webdriver
from fake_useragent import UserAgent


def user_agent() -> any:
    """Возвращает рандомный user-agent"""
    ua = UserAgent()
    return ua.random


def get_web_driver_options() -> any:
    """Возвращает опции веб драйвере"""
    option = webdriver.ChromeOptions()
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_argument('--disable-notifications')
    option.add_argument(f'--user-agent={user_agent()}')
    option.add_argument('--disable-extensions')
    option.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(os.getcwd() + "/chromedriver", options=option)
    return driver


def delay() -> None:
    """Засыпает"""
    time.sleep(random.randint(2, 4))

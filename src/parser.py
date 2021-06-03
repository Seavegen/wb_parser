""" Парсинг
"""
import pickle

from services import delay, get_web_driver_options
from config import login


driver = get_web_driver_options()


def wb_parser():
    try:
        driver.get('https://www.wildberries.ru')
        for cookie in pickle.load(open(f"cookies/{login}_cookies", "rb")):
            driver.add_cookie(cookie)
        delay()
        driver.refresh()
        delay()
    except Exception as error:
        print(error)

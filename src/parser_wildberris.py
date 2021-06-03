""" Парсинг
"""
import pickle
import csv

from services import delay, get_web_driver_options
from config import login


driver = get_web_driver_options()


def wb_parser(driver):
    try:
        driver.get('https://www.wildberries.ru')
        for cookie in pickle.load(open(f"cookies/{login}_cookies", "rb")):
            driver.add_cookie(cookie)
        delay()
        driver.refresh()
        delay()
        with open('data_csv/id.csv', newline='\n') as f:
            reader = csv.reader(f)
            for row in reader:
                id_link = row[0]
                driver.get(f'https://www.wildberries.ru/catalog/{id_link}/detail.aspx')

    except Exception as error:
        print(error)


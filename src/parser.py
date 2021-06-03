""" Парсинг
"""
import pickle
import csv

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

        vendor_code = ''
        with open('data_csv/id.csv', newline='\n') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

        # driver.get(f'https://www.wildberries.ru/catalog/{vendor_code}/detail.aspx')

    except Exception as error:
        print(error)


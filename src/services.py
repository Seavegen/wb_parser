""" Сервисы
"""
import random
import time

from fake_useragent import UserAgent


def user_agent() -> any:
    """Возвращает рандомный user-agent"""
    ua = UserAgent()
    return ua.random


def delay() -> None:
    """Засыпает"""
    time.sleep(random.randint(2, 4))

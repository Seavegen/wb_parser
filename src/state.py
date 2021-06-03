from aiogram.dispatcher.filters.state import StatesGroup, State


class CaptchaAndPhoneState(StatesGroup):
    """Стейт для отправки капчи и кода с СМС"""
    captcha = State()
    phone = State()

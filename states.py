from aiogram.dispatcher.filters.state import StatesGroup, State


class Data(StatesGroup):
    message = State()
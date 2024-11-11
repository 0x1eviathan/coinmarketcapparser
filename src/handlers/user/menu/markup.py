from aiogram import types 
from aiogram.utils.keyboard import InlineKeyboardBuilder


def menu_markup(is_enabled: bool):
    builder = InlineKeyboardBuilder()
    
    if is_enabled:
        builder.add(
            types.InlineKeyboardButton(
                text='Состояние: Включено',
                callback_data='state:on'
            )
        )
    else: 
        builder.add(
            types.InlineKeyboardButton(
                text='Состояние: Выключено',
                callback_data='state:off'
            )
        )
    
    return builder.as_markup()

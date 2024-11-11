from src.api.database import database_api
from .markup import menu_markup

from src.loader import user_router

from aiogram import filters, types 


@user_router.message(filters.CommandStart())
async def start_command_handler(message: types.Message):
    chat_id = message.from_user.id 
    
    user = await database_api.user.get(chat_id=chat_id) 
    
    is_enabled = user.is_enabled
    
    await message.answer(
        text=f'Приветствую, {message.from_user.full_name}!\n\n' \
             '' \
             f'Чтобы воспользоваться возомжностями бота - нажми на кнопочку под сообщением.',
        reply_markup=menu_markup(is_enabled=is_enabled)
    )

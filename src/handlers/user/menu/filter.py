from src.loader import redis

from aiogram import filters, types 


class IsEnabledParseFilter(filters.BaseFilter):
    async def __call__(self, callback: types.CallbackQuery): 
        chat_id = callback.from_user.id 
        
        is_enable = True if redis.get(f'{chat_id}') else False 
        
        if is_enable:
            return True
        
        return False

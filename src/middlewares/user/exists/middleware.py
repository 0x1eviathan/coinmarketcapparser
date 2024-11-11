from src.api.database import database_api

from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class ExistsMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        chat_id = event.from_user.id
        
        user = await database_api.user.get(chat_id=chat_id) 
        
        if not user: 
            await database_api.user.add(chat_id=chat_id) 
            
        return await handler(event, data)
        
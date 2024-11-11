import asyncio 

from .api.database import database_api
from .handlers import user_router
from .handlers.user.menu.parser import parse_coins

from .loader import bot, scheduler
from .logger import setup_logger

from aiogram import Dispatcher


async def on_startup(): 
    await database_api.init_models()
    scheduler.start()

    # await parse_coins()


async def main():
    await on_startup() 
    
    dp = Dispatcher() 
    
    dp.include_router(user_router)
    
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot) 
    

if __name__ == '__main__': 
    setup_logger()
    asyncio.run(main())

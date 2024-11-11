import redis 

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from .middlewares import ExistsMiddleware

from .config import settings

from aiogram import Bot, Router 
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

redis = redis.StrictRedis(host='localhost', port=6379, db=0)
redis.flushall()

bot = Bot(token=settings.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

scheduler = AsyncIOScheduler()

user_router = Router() 
user_router.message.outer_middleware(ExistsMiddleware())

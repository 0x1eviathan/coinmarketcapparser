import json

from apscheduler.job import Job
from datetime import datetime

from src.api.database import database_api
from .filter import IsEnabledParseFilter
from .markup import menu_markup
from .parser import parse_coins

from src.loader import user_router, redis, scheduler

from aiogram import F, types


async def parse_job(callback: types.CallbackQuery, chat_id: int): 
    redis.set(f'{chat_id}', f'true')
        
    wait_message = await callback.message.answer(
        text='Пожалуйста, подождите...'
    )
    wait_message_id = wait_message.message_id
    
    result_path = await parse_coins(chat_id=chat_id)
    
    with open(result_path, 'r') as f:
        data = json.load(f) 
    
    response = 'Следующее уведомление будет через 3 часа.\n\n' \
                '' \
                '<blockquote>'
    
    for coin_id in data.keys(): 
        response += f'{coin_id}. {data[coin_id]['coin_name']} ${data[coin_id]['coin_price']} 24h: {data[coin_id]['coin_changes']}% Volume: ${data[coin_id]['coin_volume']}\n'
    
    response += '</blockquote>'
    
    await callback.bot.edit_message_text(
        chat_id=chat_id,
        message_id=wait_message_id,
        text=response
    )
    
    redis.delete(f'{chat_id}')


@user_router.callback_query(IsEnabledParseFilter())
async def is_enabled_parser_filter_handler(callback: types.CallbackQuery):
    await callback.answer(
        text='В данный момент парсер включен, пожалуйста, подождите.',
        show_alert=True
    )


@user_router.callback_query(F.data.startswith('state:'))
async def state_callback_handler(callback: types.CallbackQuery):
    callback_data = callback.data 
    splitted_callback_data = callback_data.split(':') 
    
    chat_id = callback.from_user.id 
    state = splitted_callback_data[1]
    
    if state == 'on':
        is_enabled = False 
        
        job = scheduler.get_job(job_id=f'{chat_id}')
        
        if job:
            scheduler.remove_job(job_id=f'{chat_id}')
    else: 
        is_enabled = True 
        
    await callback.message.edit_reply_markup(
        reply_markup=menu_markup(is_enabled=is_enabled)
    )
    
    await database_api.user.update(chat_id=chat_id, is_enabled=is_enabled)
    
    if is_enabled: 
        scheduler.add_job(func=parse_job,trigger='interval', args=[callback, chat_id],
                          seconds=15,next_run_time=datetime.now(),id=f'{chat_id}')
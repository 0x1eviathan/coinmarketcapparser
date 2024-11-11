import os 
import json

from datetime import datetime

from src.loader import user_router

from aiogram import filters, types 


@user_router.message(filters.Command('logs'))
async def logs_command_handler(message: types.Message): 
    file_names = os.listdir('result')
    
    trigger_chat_id = message.from_user.id

    flag = False
    
    for file_name in file_names: 
        splitted_file_name = file_name.split('_') 
        
        chat_id = int(splitted_file_name[0])
        timestamp = int(splitted_file_name[1].split('.')[0]) 
        
        datetime_obj = datetime.fromtimestamp(timestamp) 
        
        log_day = datetime_obj.day
        log_month = datetime_obj.strftime('%B')
        log_hour = datetime_obj.hour
        log_minute = datetime_obj.minute
        
        result_path = f'result/{file_name}'
        
        
        if trigger_chat_id == chat_id: 
            flag = True 
            
            with open(result_path, 'r') as f:
                data = json.load(f) 
            
            response = f'Последний лог {log_day} {log_month} в {log_hour}:{log_minute}.\n\n' \
                    '' \
                    '<blockquote>'
            
            for coin_id in data.keys(): 
                response += f'{coin_id}. {data[coin_id]['coin_name']} ${data[coin_id]['coin_price']} 24h: {data[coin_id]['coin_changes']}% Volume: ${data[coin_id]['coin_volume']}\n'
            
            response += '</blockquote>'
            
            await message.answer(
                text=response
            )
    
    if not flag:     
        await message.answer(
                text='В данный момент нет никаких логов. Попробуйте снова после запуска бота.'
            )

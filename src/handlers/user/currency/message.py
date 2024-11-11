import os 
import json

from src.loader import user_router

from aiogram import filters, types 


@user_router.message(filters.Command('currency'))
async def currency_command_handler(message: types.Message, command: filters.CommandObject): 
    args = command.args 
    
    if not args:
        await message.answer(
            text='Не найдено аргументов в Вашей команде. Пожалуйста, введите <code>/currency coin</code>'
        )
        
        return
    
    file_names = os.listdir('result')
    
    trigger_chat_id = message.from_user.id
    
    for file_name in file_names: 
        splitted_file_name = file_name.split('_') 
        
        chat_id = int(splitted_file_name[0])
        
        if trigger_chat_id == chat_id: 
            result_path = f'result/{file_name}'
            
            with open(result_path, 'r') as f: 
                data = json.load(f) 
                
            flag = False 
                
            for key in data.keys(): 
                if data[key]['coin_name'] == args: 
                    flag = True 
                    
                    await message.answer(
                        text='В Вашем последнем логе найдена эта монета.\n\n' \
                             '' \
                             f'<blockquote>{key}. {data[key]['coin_name']} ${data[key]['coin_price']} 24h: {data[key]['coin_changes']}% Volume: ${data[key]['coin_volume']}</blockquote>'
                    )
                    
                    return
                
            if not flag:                
                await message.answer(
                    text='В ваших логах этой монеты нет.'
                )
        else:
            await message.answer(
                text='В данный момент нет никаких логов. Попробуйте снова после запуска бота.'
            )
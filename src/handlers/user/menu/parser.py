import os
import json

from src.others import get_current_timestamp

from playwright.async_api import async_playwright


async def parse_coins(chat_id: int = 123): 
    async with async_playwright() as p: 
        browser = await p.chromium.launch(headless=True)
         
        page = await browser.new_page() 
        
        await page.goto('https://coinmarketcap.com/')
        
        tbody_element = await page.wait_for_selector('tbody')
        
        tr_elements = await tbody_element.query_selector_all('tr')
        
        result = {}
        
        for tr_element in tr_elements[:10]: 
            td_elements = await tr_element.query_selector_all('td')
            
            td_list = []
            
            for td_element in td_elements:
                td_list.append(td_element)
                
            coin_id_element = td_list[1]
            coin_id = await coin_id_element.inner_text()
            
            coin_name_element = await td_list[2].query_selector('p')
            coin_name = await coin_name_element.inner_text()
            
            coin_price_element = await td_list[3].query_selector('span')
            coin_price = await coin_price_element.inner_text()
            
            coin_changes_element = await td_list[5].query_selector('span')
            coin_changes = await coin_changes_element.inner_text()
            
            coin_volume_element = await td_list[8].query_selector('p')
            coin_volume = await coin_volume_element.inner_text()
            
            result[coin_id] = {
                'coin_name': coin_name,
                'coin_price': coin_price.replace('$', ''),
                'coin_changes': coin_changes.replace('%', ''),
                'coin_volume': coin_volume.replace('$', '')
            }
            
        current_timestamp = get_current_timestamp()
            
        result_path = f'result/{chat_id}_{current_timestamp}.json'
        
        result_names = os.listdir('result')
        
        for result_name in result_names: 
            splitted_result_name = result_name.split('_') 
            
            result_name_chat_id = int(splitted_result_name[0])
            
            if chat_id == result_name_chat_id:
                os.remove(f'result/{result_name}')
            
        with open(result_path, 'a') as f: 
            json.dump(result, f, indent=4)
        
        await browser.close()
    
    return result_path
        
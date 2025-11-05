from pprint import pprint
from telegram import Update
from telegram.ext import ContextTypes
from modules.bot import MIRROR_URL, CUSTOM_TEXT_URL, REMOTE_CONTROL_API_KEY
from requests import get, post, RequestException

async def post_request(url:str, headers: dict, json: dict = {}) -> dict:
    try:
        response = post(url, headers=headers, json=json)
        pprint(response)
        return response
    except RequestException as e:
        print(f'post_request {url} error: {e}\nheaders:{headers}')

async def get_request(url: str, headers: dict) -> dict:
    try:
        response = get(url, headers=headers)
        pprint(response)
        return response
    except RequestException as e:
        print(f'get_request {url} error: {e}\nheaders:{headers}')

async def refresh_monitor():
    headers = {
        'Content-type': 'application/json', 
        'Authorization': f'Bearer {REMOTE_CONTROL_API_KEY}'
    }

    url = f'{MIRROR_URL}/api/refresh'
    await get_request(url, headers)

async def set_monitor_power(on: bool):
    headers = {
        'Content-type': 'application/json', 
        'Authorization': f'Bearer {REMOTE_CONTROL_API_KEY}'
    }

    url = None
    if on:
        url = f'{MIRROR_URL}/api/monitor/on'
    else:
        url = f'{MIRROR_URL}/api/monitor/off'
    await post_request(url, headers) 

async def get_monitor_status() -> bool:
    headers = {
        'Content-type': 'application/json', 
        'Authorization': f'Bearer {REMOTE_CONTROL_API_KEY}'
    }

    url = f'{MIRROR_URL}/api/monitor/status'
    response = await get_request(url, headers)

async def set_brightness(level: int):
    headers = {
        'Content-type': 'application/json', 
        'Authorization': f'Bearer {REMOTE_CONTROL_API_KEY}'
    }

    url = f'{MIRROR_URL}/api/brightness/{level}'
    await get_request(url, headers)

# função de recado
async def send_message(text: str):
    headers = {
        'Content-type': 'application/json', 
        'Authorization': f'Bearer {REMOTE_CONTROL_API_KEY}'
    }
    
    await post_request(CUSTOM_TEXT_URL, headers, {'message':text})

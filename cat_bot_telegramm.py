import requests
import time
import pprint

TOKEN = '2072721110:AAEBClndY1y8B8zG9IUELYotHy_AB3a4Djc'

BOT_URL = f'https://api.telegram.org/bot{TOKEN}'

proxies = {
    'http': 'https://173.245.49.19:80',
}

url = f'{BOT_URL}/getMe'
result = requests.get(url, proxies=proxies)

print(result.text)
print(result.status_code)

url = f'{BOT_URL}/getUpdates'

while True:
    time.sleep(10)
    result = requests.get(url, proxies=proxies)
    pprint.pprint(result.json())
    messages = result.json()['result']
    for message in messages:
        chat_id = message['message']['chat']['id']
        url_send = f'{BOT_URL}/sendMessage'
        params = {
                'chat_id': chat_id,
                'text': 'Добрый день!'
                  }
        answer = requests.post(url_send, params=params, proxies=proxies)
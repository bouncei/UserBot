import requests 
import json
import pprint

bot_token = "1727697640:AAERXgE0dkMYVgAzVP-AgRr97MVuuDK4DJg"

file_id = 'BQACAgQAAxkBAAIBoGCXx0DwLZ5ZtkARRl6swCdZjKh-AAJPCwACj0u4UIQdMIOx2ctpHwQ'

r = requests.get(f'https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}')


pprint.pprint(r.json()['result']['file_path'])

r = requests.get(f'https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}')
filePath = r.json()['result']['file_path']
    
dLoad = requests.get(f'https://api.telegram.org/file/bot{bot_token}/{filePath}')

print(dLoad)
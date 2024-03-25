import requests
import time

bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'
message = '''
Please ensure that you use the correct spelling and format when searching for MOVIES/SERIES.

Example...

"Movie Desired : The Joker "Hindi"
Series Desired : Money Heist S01
                              Money Heist S02
                              Money Heist S03"
'''

def send_message(text):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    requests.post(url, params=params)

while True:
    send_message(message)
    time.sleep(3000)  # 50 minutes = 50 mins * 60 secs = 3000 seconds

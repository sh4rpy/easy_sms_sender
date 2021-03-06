import os
import time

import requests
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)


def get_status(user_id):
    access_token = os.getenv('VK_TOKEN')
    data = {
        'user_ids': user_id,
        'fields': 'online',
        'v': '5.92',
        'access_token': access_token,
    }
    response = requests.post(
        'https://api.vk.com/method/users.get', data=data
    )
    return response.json()['response'][0]['online']


def sms_sender(sms_text):
    message = client.messages.create(
        body=sms_text,
        from_='from_number',
        to='to_number'
    )
    return message.sid


if __name__ == "__main__":
    try:
        vk_id = input("Введите id ")
        while True:
            if get_status(vk_id) == 1:
                sms_sender(f'{vk_id} is online now!')
                break
            time.sleep(5)
    except KeyError:
        print('Only numbers are accepted')

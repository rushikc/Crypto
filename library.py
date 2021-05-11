import hmac
import hashlib
import base64
import json
import time
import requests
import os

#pip3 install twilio
from twilio.rest import Client
#pip3 install wappdriver
from wappdriver import WhatsApp

f = open('config.json','r')
  
# returns JSON object as 
# a dictionary
config = json.load(f)

# Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
key = config['key']
secret = config['secret']

# python3
secret_bytes = bytes(secret, encoding='utf-8')
url = config['url']

#Twilio config
account_sid = config['TWILIO_ACCOUNT_SID']
auth_token = config['TWILIO_AUTH_TOKEN']

def get_balance():
    # Generating a timestamp
    body = {"timestamp": int(round(time.time() * 1000))}
    json_body = json.dumps(body, separators = (',', ':'))
    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()
    headers = {'Content-Type': 'application/json','X-AUTH-APIKEY': key,'X-AUTH-SIGNATURE': signature}


    response = requests.post(url, data = json_body, headers = headers)
    data = response.json();
    tmp = []
    for k in data:
        if k["balance"] != '0.0':
            tmp.append(k)
    
    return tmp

def send_msg():
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Rushi.",
                     from_='whatsapp:+14155238886',
                     to='whatsapp:+917676655676'
                 )

    print(message.sid)

def send_wmsg():
    with WhatsApp() as bot:
        bot.send('Vinyas','hi - sent by a bot')


import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Load Hiddent Varibles in /.env
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_num = os.getenv('TWILIO_PHONE')
to_num = os.getenv('MY_PHONE')

# Send SMS
client = Client(account_sid, auth_token)

def send_sms(body):

    message = client.messages.create(
        body=body,
        from_=from_num,
        to=to_num
    )

    print(message.sid)
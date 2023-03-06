import os
import twilio.base.exceptions
from twilio.rest import Client

store_name = "Stacks"
body = f"Your {store_name} order is ready for pickup!\n🍟🍔➡️😋"

while True:
    rec_num = "+1" + input("Enter Cellphone number: ")
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_number = os.environ['TWILIO_NUMBER']
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
                                      body=body,
                                      from_=twilio_number,
                                      to=rec_num
                                  )
        if message.status != "queued":
            print(f"Message not sent!\nReport: {message.status}")
    except twilio.base.exceptions.TwilioRestException:
        print(f"Number: {rec_num}\nThis is not a valid number")

    print("Message sent!")

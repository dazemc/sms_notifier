import os
from twilio.rest import Client

store_name = "Stacks"
body = f"Your {store_name} order is ready for pickup!\n🍟🍔➡️😋"

def get_number():
    country_code = "+1"
    cell_num = input("Enter Cellphone number: ")
    if cell_num == "*":
        print(
            "Help:\n"
            "'*' Prints this menu\n"
            "'0000' Reboots device\n"
            "'0001' Exits program"
        )
        get_number()
    if cell_num == "0000":
        return os.system("shutdown /r /t 1")
    if cell_num == "0001":
        quit()
    else:
        return country_code + cell_num



while True:
    rec_num = get_number()
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
    except Exception as error:
        print(error)
    else:
        print("Message sent!")

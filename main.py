import os

from twilio.rest import Client

COUNTRY_CODE = "+1"
store_name = "Stacks"
body = f"Your {store_name} order is ready for pickup!\n🍟🍔➡️😋"
num_history = []


def get_number():

    global COUNTRY_CODE
    cell_num = input("Enter Cellphone number: ")
    if cell_num == "*":
        print(
            "Help:\n"
            "'*' Print this menu\n"
            "'/' List most recent numbers\n"
            "'0000' Reboot device\n"
            "'0001' Restart program\n"
            "'0002' Exit program\n"
            "'0003' View/Change country code\n"
        )
        get_number()
    if cell_num == "/":
        print(num_history[::-1])
    if cell_num == "0000":
        if os.name == "nt":
            return os.system("shutdown /r /t 1")
        if os.name == "posix":
            return os.system("sudo reboot")
    if cell_num == "0001":
        sms_loop()
    if cell_num == "0002":
        quit()
    if cell_num == "0003":
        print(f"Current Code: {COUNTRY_CODE}")
        # TODO: Add persistent data file to store last 20 numbers messaged and country code
        # new_cc = input("Enter new code, without '+', or press enter to cancel: ")
        # if new_cc != "":
        #     if new_cc[0] != "+":
        #         new_cc = "+" + new_cc
        #     COUNTRY_CODE = new_cc
        get_number()
    else:
        return COUNTRY_CODE + cell_num


def sms_loop():
    while True:
        try:
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            twilio_number = os.environ['TWILIO_NUMBER']
            # Checks for blank environ values
            if not account_sid or not auth_token or not twilio_number:
                print("One or more environment variables are blank")
                quit()
        except KeyError as error:
            print(f"Twilio API environment value {error} is missing")
            quit()

        rec_num = get_number()
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
            print(f"Twilio API Message Status:\n{error}")
        else:
            num_history.append(rec_num)
            print(f"Message sent to {rec_num.replace('+1', '')} successfully")


sms_loop()

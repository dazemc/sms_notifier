# SMS Notification App - Readme

This Python script sends SMS notifications about order readiness from a store named "Stacks" using the Twilio API. The application was designed for environments where a number pad is the primary peripheral for input.

## How to Use

You will be prompted to input a phone number to send an SMS. Enter the number without the country code. The default country code is "+1". 

If you want to use a different country code, you can change it when the program is running by entering `0003` when asked for a phone number. Then, you will be asked to enter a new country code.

Input options include:

- `*` : Print the help menu.
- `/` : List the most recent numbers the messages were sent to.
- `0000` : Reboot the device (requires the script to have sudo permissions).
- `0001` : Restart the program.
- `0002` : Exit the program.
- `0003` : View/change the current country code.
- `0004` : Change the default message. When prompted, you can type a new message or press `Enter` to cancel.

## Prerequisites

- Python 3.6+
- Twilio Python library (you can install it with `pip install twilio`)
- Twilio account with valid `account_sid`, `auth_token`, and a Twilio number.

## Environment Variables

You need to set the following environment variables:

- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID.
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token.
- `TWILIO_NUMBER`: Your Twilio phone number.

## Running the App

Run the Python script in your terminal with `python script_name.py`. 

## Note

The script does not currently persist data between runs, so the history of numbers and any changes to the country code will be reset when the program is restarted. There are placeholders in the code to implement these features at a later date. The default message can be changed while the program is running, but will also reset to the default when the program is restarted. 

The script sends an SMS with a status of "queued" and prints a confirmation message to the console. If there is an error, it will print the status returned by the Twilio API.

## Warning

The option to reboot the device is designed to work in Linux environments where the script has sudo permissions. Be careful when using this option, especially on shared or production systems.

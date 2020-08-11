def main():
    global option
    account_sid = 'AC8b7853a368a05ca88c9366360babaa7d'
    auth_token = '1e04be979634a69d66ebfbb5ca5b081e'
    client = Client(account_sid, auth_token)
    reciverr = int(input('Enter the Reciver\'s Phone Number : '))
    msg = input('Enter Your Message : ')
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=msg,
        to=f'whatsapp:+91{reciverr}'
    )

    print('Your Message Has been Sent Sucessfully.')
    while option == 'Y' or option == 'y' or option == 'yes' or option == 'Yes' or option == 'YES':
        option = input('Want to Send More Messages?? (Y/N) : ')
        if option == 'Y' or option == 'y' or option == 'yes' or option == 'Yes' or option == 'YES':
            main()


def previous():
    global option
    try:
        option = input(
            'Have You sent a WhatsApp message to this Number -> +14155238886 ?? (Y/N) : ')
        if option == 'Y' or option == 'y' or option == 'yes' or option == 'Yes' or option == 'YES':
            main()
        elif option == 'N' or option == 'n' or option == 'no' or option == 'No' or option == 'NO':
            print('\nPlease Send " join higher-pleasure " to " +14155238886 ".\nTo use this service You must have to send this text to the mentioned Number')
            print('\n')
            time.sleep(5)
            exit()
        else:
            print('Please Enter Correct Input to the Program : ')
            time.sleep(2)
            previous()
    except ValueError as e:
        pass


if __name__ == "__main__":
    from twilio.rest import Client
    import time
    option = ''
    previous()

class email_sender:
    def createAGroup(self):
        group = {}
        ch = 'y'
        while(ch != 'n'):
            gname = input('Enter name of group :')
            group[gname] = input(
                'Enter contact emails separated by a single space :').rstrip()
            ch = input('Add another....y/n? :').rstrip()
        with open('groups.json', 'a') as f:
            json.dump(group, f)

    def sendmail(self, sender_add, reciever_add, msg, password):
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(sender_add, password)
        server.sendmail(sender_add, reciever_add, msg)
        print("Mail sent succesfully....!")

    def sendEmailToAGroup(self):
        gname = input('Enter name of group :')
        members = ''
        try:
            f = open('groups.json', 'r')
            members = json.load(f)
            f.close()
        except:
            print('Invalid group name. Please Create group first')
            exit
        for i in members:
            print(i)
        time.sleep(5)
        members = members[gname].split()
        msg = input('Enter message :')
        for i in members:
            try:
                sendmail(your_add, i, msg, password)
            except:
                print("An unexpected error occured. Please try again later...")
                continue

    def login(self):
        emailtemp = str(input('Enter Your Email Address : '))
        pas = str(input('Enter Your Password : '))
        if emailtemp.split('@')[1].split('.')[1] == 'com':
            email = emailtemp
        return email, pas

    def sendEmailToAnIndividual(self):
        emaill, password = email_sender.login('Get Login Here')
        emaill_address_temp = input('Enter the Recivers Email Address : ')
        if emaill_address_temp.split('@')[1].split('.')[1] == 'com':
            emaill_address = emaill_address_temp
        else:
            emaill_address = 'alexmercerr07@gmail.com'
        sub = input('Enter Your Subject for this E-Mail : ')
        msg_temp = input('Enter Your Message : ')
        msg = f"""Subject : {sub}\n\n{msg_temp}"""
        val = email_sender.sendmail(
            'Send the mail', emaill, emaill_address, msg, password)
        print(val)
        print('Mail has been sucessfully Sent')

    def view(self):
        os.system('cls')
        print('|____________________________________________________|')
        print('------------------Welcome to Email Sender------------|')
        print('|====================================================|')
        print('1. Create a Group to email Multiple Users at once')
        print('2. Send Email to An Individual Person')
        print('3. Send Mail to a Group')
        print('4. Exit/Quit')

    def header(self):
        print('|____________________________________________________|')
        print('--------------------Email Sender---------------------|')
        print('|====================================================|')


def main():
    email_sender.view('firstProcess')
    try:
        inputNumber = int(input('Enter Your Dezired Operation Number : '))
    except ValueError as e:
        print('Enter Correct Number')
        time.sleep(2)
        main()
    while inputNumber > 0 and inputNumber < 5:
        if inputNumber == 1:
            email_sender.createAGroup('Create a Group')
        elif inputNumber == 2:
            email_sender.sendEmailToAnIndividual('Email to Individual')
        elif inputNumber == 3:
            email_sender.sendEmailToAGroup('Email to a Group')
        elif inputNumber == 4:
            exit()

        inputNumber = input('Want to Send More Emails?? : ')
        if inputNumber == 'No' or inputNumber == 'no' or inputNumber == 'N' or inputNumber == 'n' or inputNumber == 'NO':
            exit()
    else:
        print('Enter Correct Number')
        time.sleep(2)
        main()


if __name__ == "__main__":
    import smtplib
    import json
    import time
    import os
    os.chdir('Send Emails with Python')
    haveToIncludeComma = False
    main()

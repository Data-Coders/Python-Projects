import smtplib
import json
import time
import os


class email_sender:
    def createAGroup(self):
        email = {}
        os.chdir('Send Emails with Python')
        with open('groups.json', 'a') as fileObj:
            try:
                group = str(input('Enter The Name of Group : '))
                numberOfEmailAddress = int(
                    input('Enter The Number of Participants to add in a Group : '))
            except ValueError as e:
                print(
                    'Please Enter Correct Value for this (You  Have to Enter Number of Participants in Integers)')

            for i in range(0, numberOfEmailAddress):
                try:
                    emailaddresstemp = input('Enter The Email Address : ')
                    if emailaddresstemp.split('@')[1].split('.')[1] == 'com':
                        email[group] = emailaddresstemp
                        inserted = True
                except ValueError as e:
                    print('Enter The Correct Email Address')
                    email_sender.createAGroup()
            if inserted == True:
                json.dump(email, fileObj)

    def sendEmailToAGroup(self):
        print('This is function 2')

    def sendEmailToAnIndividual(self):
        print('This is function 3')

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

        try:
            inputNumber = int(input('Want to Send More Emails??'))
        except ValueError as e:
            print('Enter The Input Correctly')
            time.sleep(2)
            main()

    else:
        print('Enter Correct Number')
        time.sleep(2)
        main()


if __name__ == "__main__":
    main()

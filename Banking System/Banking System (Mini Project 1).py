class bank:
    def openBankAccount(self):
        os.system('cls')
        bank.header('Header of The Function 1')
        numberOfCustomers = int(input('Enter the Number Of Customers : '))
        for i in range(0, numberOfCustomers):
            name = str(input('Enter The Full Name : '))
            pin = int(input(
                'Please Input PIN of your Choice (Please Keep it Private for Security Reason) : '))
            amount = int(input('Enter the amount to deposit amount : '))
            accountNo = int(random.randint(11, 99))
            with open('accountzWithDetails.txt', 'a') as fileObj:
                data = f'Name ->{name}->PIN ->{pin}->Amount ->{amount}->Account Number ->{accountNo}->\n'
                fileObj.write(data)
                print('Account Created with Dezired Credentials')
                print(
                    f'Your Account Number is {accountNo} with PIN number {pin}\n\n Please Note This as this will be asked next time whenever you want to make a Deposit or WithDrwal')
                time.sleep(3)
        main()

    def withdraw(self):
        os.system('cls')
        bank.header('Header')
        newAmount = 0
        accountNo = int(input('Enter Your Account Number : '))
        pinno = int(input('Enter Your Pin : '))
        with open('accountzWithDetails.txt', 'r') as fileObj:
            with open('accountz.txt', 'a') as fileObjTemp:
                for line in fileObj:
                    if line.split('->')[7] == str(accountNo):
                        if line.split('->')[3] == str(pinno):
                            enteredAmount = int(
                                input('Enter The Amount to be Deposited : '))
                            if int(line.split('->')[5]) > enteredAmount:
                                oldAmount = int(line.split('->')[5])
                                newAmount = oldAmount - enteredAmount
                                name = line.split('->')[1]
                                pin = pinno
                                amount = newAmount
                                data = f'Name ->{name}->PIN ->{pin}->Amount ->{amount}->Account Number->{accountNo}->\n'
                                fileObjTemp.write(data)
                            else:
                                print(
                                    '''Your Account doesn't have That much of Amount''')
                                main()
                        else:
                            data = line
                            fileObjTemp.write(data)
                    else:
                        data = line
                        fileObjTemp.write(data)
        os.remove('accountzWithDetails.txt')
        os.rename(r'accountz.txt', r'accountzWithDetails.txt')

        print('Authenticating')
        time.sleep(0.5)
        print('Authenticated!!')
        print('Updating The Amount')
        time.sleep(1)
        print('Updated The Amount')
        main()

    def deposit(self):
        os.system('cls')
        bank.header('Header')
        newAmount = 0
        accountNo = int(input('Enter Your Account Number : '))
        pinno = int(input('Enter Your Pin : '))
        with open('accountzWithDetails.txt', 'r') as fileObj:
            with open('accountz.txt', 'a') as fileObjTemp:
                for line in fileObj:
                    if line.split('->')[7] == str(accountNo):
                        if line.split('->')[3] == str(pinno):
                            enteredAmount = int(
                                input('Enter The Amount to be Deposited : '))
                            oldAmount = int(line.split('->')[5])
                            newAmount = enteredAmount + oldAmount
                            name = line.split('->')[1]
                            pin = pinno
                            amount = newAmount
                            data = f'Name->{name}->PIN->{pin}->Amount->{amount}->Account Number->{accountNo}->\n'
                            fileObjTemp.write(data)
                        else:
                            data = line
                            fileObjTemp.write(data)
                    else:
                        data = line
                        fileObjTemp.write(data)
        os.remove('accountzWithDetails.txt')
        os.rename(r'accountz.txt', r'accountzWithDetails.txt')

        print('Authenticating')
        time.sleep(0.5)
        print('Authenticated!!')
        print('Updating The Amount')
        time.sleep(1)
        print('Updated The Amount')
        main()

    def spacee(self, nameOftheParameter, numberThatSpace):
        rightwalaSpace = ''
        leftwalaSpace = ''
        for i in (0, numberThatSpace):
            numberOfSpace = numberThatSpace - len(nameOftheParameter)
            if (len(nameOftheParameter) % 2) != 0:
                numberOfSpace = numberOfSpace + 1
            leftSpace = numberOfSpace / 2
            leftwalaSpace = ' ' * int(leftSpace)
            if (len(nameOftheParameter) % 2) == 0:
                leftwalaSpace = leftwalaSpace + ' '
            rightSpace = numberOfSpace / 2
            rightwalaSpace = ' ' * int(rightSpace)
        return rightwalaSpace, leftwalaSpace

    def checkCustomersAndBalance(self):
        os.system('cls')
        bank.header('Header')
        with open('accountzWithDetails.txt', 'r') as fileObj:
            print(
                ' _____________________________________________________________________ ')
            print(
                '|            Name           |  Account Number   |  PIN    |  Amount   |')
            print(
                '|---------------------------------------------------------------------|')
            for line in fileObj:
                leftwalaSpace = ''
                rightwalaSpace = ''
                name = line.split('->')[1]
                accountNo = line.split('->')[7]
                pinno = line.split('->')[3]
                ammount = line.split('->')[5]
                rightwalaSpace, leftwalaSpace = bank.spacee(
                    'To Get the Space', name, 26)
                accountwalaRight, accountwalaLeft = bank.spacee(
                    'To get the space for account variable', accountNo, 18)
                pinwalaRight, pinwalaLeft = bank.spacee(
                    'To get the Space', pinno, 8)
                ammountwalaRight, ammountwalaLeft = bank.spacee(
                    'To get the Space', ammount, 10)
                print(
                    f'|{leftwalaSpace}{name}{rightwalaSpace}|{accountwalaLeft}{accountNo}{accountwalaRight}|{pinwalaLeft}{pinno}{pinwalaRight}|{ammountwalaLeft}{ammount}{ammountwalaRight}|')
                # print(name)
        print('|_____________________________________________________________________|')
        time.sleep(5)
        main()

    def view(self):
        os.system('cls')
        print('=======================================================================')
        print(' ------------------------Welcome to Times Bank------------------------ ')
        print('***********************************************************************')
        print('=<< 1. Open a New Account                                           >>=')
        print('=<< 2. Withdraw Money                                               >>=')
        print('=<< 3. Deposit Money                                                >>=')
        print('=<< 4. Check Customers and Balance                                  >>=')
        print('=<< 5. Delete the DataBase                                          >>=')
        print('=<< 6. Exit/Quit                                                    >>=')
        print('***********************************************************************')

    def header(self):
        os.system('cls')
        print('=======================================================================')
        print(' ------------------------Welcome to Times Bank------------------------ ')
        print('***********************************************************************')

    def delthedatabase(self):
        os.system('cls')
        bank.header('Displaying the Data')
        os.remove('accountzWithDetails.txt')
        time.sleep(5)
        main()


def main():
    os.system('cls')
    bank.view('view')
    inputNumber = int(
        input('Select Your Choice Number from the Above Menu : '))
    if inputNumber == 1:
        bank.openBankAccount('Open Bank Account')
    elif inputNumber == 2:
        bank.withdraw('Withdrawing The Amount')
    elif inputNumber == 3:
        bank.deposit('Depositing The Amount')
    elif inputNumber == 4:
        bank.checkCustomersAndBalance(
            'Viewing all The Customers Account Balance')
    elif inputNumber == 6:
        exit
    elif inputNumber == 5:
        bank.delthedatabase('Deleting the DataBase')
    else:
        print('Please Enter The Correct Option (i.e. from 1 - 5) : ')


if __name__ == "__main__":
    try:
        import os
        import random
        import time
    except ModuleNotFoundError as e:
        os.system('pip install time')
    finally:
        main()

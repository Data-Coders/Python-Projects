class bank:
    def openBankAccount(self):
        os.system('cls')
        bank.header('Header of The Function 1')
        try:
            numberOfCustomers = int(input('Enter the Number Of Customers : '))
        except ValueError as e:
            print('Please Enter Number Of Customers Here')
            time.sleep(1)
            bank.openBankAccount('Got Error in NoOfCustomers')
        for i in range(0, numberOfCustomers):
            try:
                name = str(input('Enter The Full Name : '))
            except ValueError as e:
                print('Please Enter Name which only Contains English Alphabets')
                bank.openBankAccount('Got Error')
            try:
                pin = int(input(
                    'Please Input PIN of your Choice (Please Keep it Private for Security Reason) : '))
                if len(str(pin)) > 4:
                    print('Please Select PIN with the Length of 4 no less no more')
                    time.sleep(1)
                    bank.openBankAccount('Got Error')
                elif len(str(pin)) < 4:
                    print('Please Select PIN with the Length of 4 no more no less')
                    time.sleep(1)
                    bank.openBankAccount('Got Error')
            except ValueError as e:
                print('Please Enter PIN in Numbers as it will be easy to work for You')
                time.sleep(1)
                bank.openBankAccount('Got Error')
            try:
                amount = int(
                    input('Enter the amount to deposit amount (Max of 10 Billion) : '))
            except ValueError as e:
                print('Enter Amount in Numbers not in Alphabets')
                time.sleep(1)
                bank.openBankAccount('Got Error')
            accountNo = int(random.randint(11, 99))
            with open('accountzWithDetails.txt', 'a') as fileObj:
                data = f'Name ->{name}->PIN ->{pin}->Amount ->{amount}->Account Number ->{accountNo}->\n'
                fileObj.write(data)
                print('Account Created with Dezired Credentials')
                print(
                    f'Your Account Number is {accountNo} with PIN number {pin}\n\n Please Note This as this will be asked next time whenever you want to make a Deposit or WithDrwal \n')
                time.sleep(3)
            fileObj.close()
        main()

    def withdraw(self):
        notUpdated = True
        idpass = True
        os.system('cls')
        bank.header('Header')
        accountNo = ''
        newAmount = 0
        try:
            accountNumberorName = input('Enter Your Account Number : ')
            with open('accountzwithDetails.txt', 'r') as FileObj:
                for line in FileObj:
                    if accountNumberorName == line.split('->')[1]:
                        accountNo = line.split('->')[1]
                    try:
                        if int(accountNumberorName) == int(line.split('->')[7]):
                            accountNo = line.split('->')[7]
                    except ValueError as e:
                        pass
            FileObj.close()
        except ValueError as er:
            print('Please Enter Correct Details as Per on the Records on our Servers.')
            time.sleep(2)
            main()
        try:
            pinno = int(input('Enter Your Pin : '))
        except ValueError as e:
            print(
                'Each and Every PIN numbers stored in our Servers are in form of Numbers not as Alpabets')
            time.sleep(2)
            bank.withdraw('Got Error')
        with open('accountzWithDetails.txt', 'r') as fileObj:
            with open('accountz.txt', 'a') as fileObjTemp:
                for line in fileObj:
                    if line.split('->')[7] == str(accountNo) or line.split('->')[1] == str(accountNo):
                        if line.split('->')[3] == str(pinno):
                            try:
                                enteredAmount = int(
                                    input('Enter The Amount to be Withdrawn : '))
                            except ValueError as e:
                                print('Amount Must be in Numbers not Alpabets')
                                bank.withdraw()
                            if int(line.split('->')[5]) >= enteredAmount:
                                oldAmount = int(line.split('->')[5])
                                newAmount = oldAmount - enteredAmount
                                name = line.split('->')[1]
                                pin = pinno
                                amount = newAmount
                                accountNotemp = line.split('->')[7]
                                data = f'Name ->{name}->PIN ->{pin}->Amount ->{amount}->Account Number->{accountNotemp}->\n'
                                fileObjTemp.write(data)
                                notUpdated = False
                            else:
                                print(
                                    '''Your Account doesn't have That much of Amount''')
                                name = line.split('->')[1]
                                pin = pinno
                                amount = int(line.split('->')[5])
                                accountNotemp = line.split('->')[7]
                                data = f'Name ->{name}->PIN ->{pin}->Amount ->{amount}->Account Number->{accountNotemp}->\n'
                                fileObjTemp.write(data)
                                time.sleep(1)
                                notUpdated = True
                        else:
                            if notUpdated == True:
                                idpass = False
                                notUpdated = True
                            data = line
                            fileObjTemp.write(data)
                    else:
                        if notUpdated == True:
                            idpass = False
                            notUpdated = True
                        data = line
                        fileObjTemp.write(data)
            fileObjTemp.close()
        fileObj.close()
        if notUpdated == False:
            os.remove('accountzWithDetails.txt')
            os.rename(r'accountz.txt', r'accountzWithDetails.txt')

            print('Authenticating')
            time.sleep(0.5)
            print('Authenticated!!')
            print('Updating The Amount')
            time.sleep(1)
            print('Updated The Amount')
            main()
        elif notUpdated == True:
            os.remove('accountzWithDetails.txt')
            os.rename(r'accountz.txt', r'accountzWithDetails.txt')
            time.sleep(1)
            if idpass == True:
                print(
                    'Authenticated But Input Amount is Over-Valued as compared to Your Account')
            else:
                print(
                    'Error in Authenticating with Our Servers. \nFull Name/Account Number or PIN is incorrect')
            time.sleep(1)
            main()

    def errorr(self):
        if self == 'PIN':
            print('Please Enter The correct PIN Number')
        elif self == 'Name or Account Number':
            print('Enter The Correct Bank Account Number')
        else:
            main()

    def deposit(self):
        notUpdated = True
        os.system('cls')
        bank.header('Header')
        accountNo = ''
        pinno = 0
        newAmount = 0
        accountNumberorName = input('Enter Your Account Number : ')
        with open('accountzwithDetails.txt', 'r') as FileObj:
            for line in FileObj:
                if accountNumberorName == line.split('->')[1]:
                    accountNo = line.split('->')[1]
                try:
                    if int(accountNumberorName) == int(line.split('->')[7]):
                        accountNo = line.split('->')[7]
                except ValueError as e:
                    pass
        FileObj.close()

        try:
            pinnotemp = int(input('Enter Your Pin : '))
            if len(str(pinnotemp)) == 4:
                pinno = pinnotemp
            elif len(str(pinnotemp)) > 4:
                print(
                    f'Please Enter You PIN correctly as PIN should be 4 digits long not {len(str(pinnotemp))}')
                time.sleep(1)
                bank.deposit('Got error on PIN length')
            elif len(str(pinnotemp)) < 4:
                print(
                    f'Please Enter You PIN correctly as PIN should be 4 digits long not {len(str(pinnotemp))}')
                time.sleep(1)
                bank.deposit('Got error on PIN length')
        except ValueError as e:
            print('Enter the PIN in Numbers')
            time.sleep(1)
            bank.deposit('Got an Error in PIN')
        with open('accountzWithDetails.txt', 'r') as fileObj:
            with open('accountz.txt', 'a') as fileObjTemp:
                for line in fileObj:
                    if line.split('->')[7] == str(accountNo) or line.split('->')[1] == accountNo:
                        if line.split('->')[3] == str(pinno):
                            try:
                                enteredAmount = int(
                                    input('Enter The Amount to be Deposited : '))
                            except ValueError as e:
                                print(
                                    'Please Enter The Amount in Digit Not in Alphabets')
                                time.sleep(1)
                                bank.deposit('Got Error on Deposit Amount')
                            oldAmount = int(line.split('->')[5])
                            newAmounttemp = enteredAmount + oldAmount
                            if newAmounttemp > 10000000000:
                                print(
                                    f'Your Entered Amount is way more to handle our Servers.\nPlease Contact {ITname} for getting this Error Resolved.\nThank You')
                                time.sleep(1)
                                fileObj.close()
                                fileObjTemp.close()
                                main()
                            elif newAmounttemp < 10000000000 and newAmounttemp > 0:
                                newAmount = newAmounttemp
                            name = line.split('->')[1]
                            pin = pinno
                            amount = newAmount
                            accountNotemp = line.split('->')[7]
                            data = f'Name->{name}->PIN->{pin}->Amount->{amount}->Account Number->{accountNotemp}->\n'
                            fileObjTemp.write(data)
                            notUpdated = False
                        else:
                            if notUpdated == True:
                                idpass = False
                                notUpdated = True
                            data = line
                            fileObjTemp.write(data)
                    else:
                        if notUpdated == True:
                            idpass = False
                            notUpdated = True
                        data = line
                        fileObjTemp.write(data)
            fileObjTemp.close()
        fileObj.close()
        if notUpdated == False:
            os.remove('accountzWithDetails.txt')
            os.rename(r'accountz.txt', r'accountzWithDetails.txt')

            print('Authenticating')
            time.sleep(0.5)
            print('Authenticated!!')
            print('Updating The Amount')
            time.sleep(1)
            print('Updated The Amount')
            main()
        elif notUpdated == True:
            os.remove('accountzWithDetails.txt')
            os.rename(r'accountz.txt', r'accountzWithDetails.txt')
            time.sleep(1)
            if idpass == True:
                print(
                    'Authenticated But Input Amount is Over-Valued as compared to Your Account')
            else:
                print(
                    'Error in Authenticating with Our Servers. \nFull Name/Account Number or PIN is incorrect')
            time.sleep(1)
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
        try:
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
            print(
                '|_____________________________________________________________________|')
            time.sleep(3)
            fileObj.close()
            main()
        except FileNotFoundError as e:
            print(
                ' _____________________________________________________________________ ')
            print(
                '|            Name           |  Account Number   |  PIN    |  Amount   |')
            print(
                '|---------------------------------------------------------------------|')
            print(
                '|DataBase is Currently Empty|        -          |   -     |     -     |')
            print(
                ' _____________________________________________________________________ \n\nEnter Some Records To see Your Records Here')
            time.sleep(3)
            main()

    def view(self):
        try:
            os.remove('accountz.txt')
        except FileNotFoundError as e:
            pass
        except PermissionError as e:
            pass
        os.system('cls')
        print('=======================================================================')
        print(' ------------------------Welcome to Times Bank------------------------ ')
        print('***********************************************************************')
        print('=<< 1. Open a New Account                                           >>=')
        print('=<< 2. Withdraw Money                                               >>=')
        print('=<< 3. Deposit Money                                                >>=')
        print('=<< 4. Check Customers and Balance                                  >>=')
        print('=<< 5. Delete the DataBase                                          >>=')
        print('=<< 6. Delete a Particular Customer                                 >>=')
        print('=<< 7. Exit/Quit                                                    >>=')
        print('***********************************************************************')

    def header(self):
        os.system('cls')
        print('=======================================================================')
        print(' ------------------------Welcome to Times Bank------------------------ ')
        print('***********************************************************************')

    def headerr(self):
        os.system('cls')
        print('=======================================================================')
        print(' ------------------------Welcome to Times Bank------------------------ ')
        print('***********************************************************************')
        a = self
        a1 = ''
        for i in range(1, 5):
            os.system('cls')
            bank.header('just to display the meaning')
            a1 = a1 + '.'
            time.sleep(0.1)
            print(a)

    def delthedatabase(self):
        os.system('cls')
        bank.headerr(
            'Infecting the Server with BlackWatch Virus and Deleting the DataBase')
        try:
            os.remove('accountzWithDetails.txt')
        except FileNotFoundError as e:
            pass
        time.sleep(5)
        main()

    def deleteaParticular(self):
        os.system('cls')
        bank.header('Heading')
        try:
            name = str(input('Enter The Account Holder Name/Account Number'))
        except ValueError as e:
            pass
        with open('accountzWithDetails.txt', 'r') as fileObj:
            with open('accountz.txt', 'a') as fileObjtemp:
                for line in fileObj:
                    if line.split('->')[1] == name or line.split('->')[7]:
                        pass
                    else:
                        fileObjtemp.write(line)
            fileObjtemp.close()
        fileObj.close()
        os.remove('accountzWithDetails.txt')
        os.rename(r'accountz.txt', r'accountzWithDetails.txt')
        main()


def main():
    os.system('cls')
    try:
        os.remove('accountz.txt')
    except FileNotFoundError as e:
        pass
    except PermissionError as e:
        bank.view('View')
    bank.view('view')
    try:
        inputNumber = int(
            input('Select Your Choice Number from the Above Menu : '))
    except ValueError as e:
        print('Enter the choice in Numbers')
        time.sleep(1)
        main()
    if inputNumber == 1:
        bank.openBankAccount('Open Bank Account')
    elif inputNumber == 2:
        bank.withdraw('Withdrawing The Amount')
    elif inputNumber == 3:
        bank.deposit('Depositing The Amount')
    elif inputNumber == 4:
        bank.checkCustomersAndBalance(
            'Viewing all The Customers Account Balance')
    elif inputNumber == 7:
        exit()
    elif inputNumber == 5:
        bank.delthedatabase('Deleting the DataBase')
    elif inputNumber == 6:
        bank.deleteaParticular('Deleting a Particular User Account')
    else:
        print('Please Enter The Correct Option (i.e. from 1 - 5)')
        time.sleep(1)
        main()


if __name__ == "__main__":
    try:
        import os
        import random
        import time
    except ModuleNotFoundError as e:
        os.system('pip install time')
    finally:
        ITname = '''Admin'''
        main()

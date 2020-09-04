class operations:
    def add(self):
        summ = 0
        try:
            noOfNumberToAdd = int(input('Enter the Number of Numbers to ADD : '))
        except ValueError as e:
            print('Enter the Number in Integers')
            operations.add('Again Add')
        for i in range(0,noOfNumberToAdd):
            try:
                number = int(input('Enter The Number : '))
            except ValueError as e:
                print('Enter The Number in Integer')
            summ = summ + number
        return summ

    def sub(self):
        result = 0
        try:
            firstNumber = int(input('Enter The First Number : '))
            secondNumber = int(input('Enter The Second Number : '))
        except ValueError as e:
            print('Enter the Number in Integers')
        if firstNumber < secondNumber:
            print('The result will be in Negetive Do You Still want the Result', end='')
            inpuut = str(input(' Y/N : '))
            if inpuut == 'Y':
                result = firstNumber - secondNumber
        else:
            result = firstNumber - secondNumber
        return result

    def multi(self):
        result = 1
        try:
            noOfNumberToAdd = int(input('Enter the Number of Numbers to Multiply : '))
        except ValueError as e:
            print('Enter the Number in Integers')
            operations.multi('Again Multi')
        for i in range(0,noOfNumberToAdd):
            try:
                number = int(input('Enter The Number : '))
            except ValueError as e:
                print('Enter The Number in Integer')
            result = result * number
        return result
        

    def div(self):
        try:
            firstNumber = int(input('Enter The First Number : '))
            secondNumber = int(input('Enter The Second Number : '))
        except ValueError as e:
            print('Enter the Number in Integers')
        return firstNumber / secondNumber

def main():
    print('|______________________________________________________________|')
    print('|--------------Welcome to Command Line Calculator--------------|')
    print('|--------------------------------------------------------------|')
    print('| 1. Add Numbers                                               |')
    print('| 2. Substract Numbers                                         |')
    print('| 3. Multiply Numbers                                          |')
    print('| 4. Divide Numbers                                            |')
    print('| 5. Exit                                                      |')
    print('|--------------------------------------------------------------|')
    try:
        UserInput = int(input('Enter The Option Number Based on Your Choice : '))
    except ValueError as e:
        print('Please Enter the Correct Input')
        main()
    if UserInput == 1:
        result = operations.add('add')
        print(f'Your Sum of two Numbers is {result}')
        time.sleep(4)
        main()
    if UserInput == 2:
        result = operations.sub('Substract')
        print(f'Your Diffrence of two Numbers is {result}')
        time.sleep(4)
        main()
    if UserInput == 3:
        result = operations.multi('Multiply')
        print(f'Your Product of two Numbers is {result}')
        time.sleep(4)
        main()
    if UserInput == 4:
        result = operations.div('Divide')
        print(f'Your Dividend of two Numbers is {result}')
        time.sleep(4)
        main()
    if UserInput == 5:
        exit()

if __name__ == "__main__":
    import time
    main()
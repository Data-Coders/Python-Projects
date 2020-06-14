sum = 0
number = 0
while (True):
    userInput = input('\n Enter Your Number : ')
    if userInput == 'q' or userInput == 'Q':
        print(sum)
        exit(0)
    else:
        number = int(userInput)
        sum += number

sum = 0
ls = []
while (True):
    userItemNumber = int(input('\n Enter the Item Number : '))
    userPrice = input('\n Enter The Price : ')
    if userItemNumber == 'q' or userItemNumber == 'Q':
        print(ls)
        exit(0)
    else:
        price = int(userPrice)
        itemNumber = int(userItemNumber)
        sum += price
        print(sum)
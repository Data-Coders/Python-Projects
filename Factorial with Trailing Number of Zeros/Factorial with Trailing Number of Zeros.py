# Question 1

# Part 1 : Find the Factorial of a number
# Part 2 : Find the Number of Trailing Zeros in Factorial

def calculate(num):
    count = 0
    n = factorial(num)
    while (n % 10 == 0):
        count = count + 1
        n = n / 10
    return count


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


if __name__ == '__main__':
    num = int(input("\n Enter a Number : "))
    fac = factorial(num)
    print(f"Your Factorial of {num} is {fac}")
    calc = calculate(num)
    print(f"Your Factorial Trailing Zeros of {num} is {calc}")

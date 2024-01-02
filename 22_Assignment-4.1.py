# 1. WAP to find the factorial of a given number.

num = int(input('Enter a number: '))
factorial = 1

if num >= 0:
    if num != 0:
        for i in range(num, 0, -1):
            factorial *= i
    print(f"{num}! = {factorial}")
else:
    print("Error!")
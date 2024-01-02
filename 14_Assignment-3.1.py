# 1. Write a program to check input number is even or odd.

num = int(input('Enter a number: '))

if num % 2 == 0:
    print(f"{num}, is an even number.")
else:
    print(f"{num}, is an odd number.")
# 2. Write a python program to find the greatest number among three.

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = int(input('Enter 3rd number: '))

if num1 > num2 and num1 > num3:
    print(f"{num1}, is greatest among {num1, num2, num3}.")
elif num2 > num3:
    print(f"{num2}, is greatest among {num1, num2, num3}.")
else:
    print(f"{num3}, is greatest among {num1, num2, num3}.")
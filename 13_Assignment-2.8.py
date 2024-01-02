''' Write a program to perform the addition & substraction of two numbers without using their corresponding operator.'''

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

print(f"{num1} + {num2} = {num1 - (-num2)}")
print(f"{num1} - {num2} = {(((num1 // num2) -1) * num2) + (num1 % num2)}")
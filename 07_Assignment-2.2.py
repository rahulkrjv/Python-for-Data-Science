''' Write a Python program that read a 5-digit number from user and perform the sum of first and last digit (without loop).'''

num = int(input('Enter a 5-digit number: '))

unitDigit = num % 10
lastDigit = num // 10000

print(f"Sum of first & last digit of {num} is: {unitDigit + lastDigit}")
''' Write a Python program that read a 3-digit number from user and perform the addition of their digits (without loop). E.g (If user enter a number 367 then result is 16)'''

num = int(input('Enter a 3-digit number: '))

unitDigit = num % 10
tensDigit = (num % 100) // 10
hunDigit = (num % 1000)// 100

print(f"Sum of digits of, {num} is: {unitDigit + tensDigit + hunDigit}")
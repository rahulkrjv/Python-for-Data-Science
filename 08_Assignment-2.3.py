''' Write a Python program that read a 4-digit number from user and reverse that number (without loop).'''

num = int(input('Enter a 4-digit number: '))

reverseNum = int(str(num)[::-1])

print (f"Reverse of {num} is: {reverseNum}")
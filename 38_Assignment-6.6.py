# 6. Write a Python program to reverse a string if it's length is a multiple of 4.

str = input('Enter string: ')

if len(str) % 4 == 0:
    str = str[-1::-1]

print('New string: ', str)
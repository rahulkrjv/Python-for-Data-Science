'''
2. Write a Python program to get a string made of the first 2 and the last 2
chars from a given a string. If the string length is less than 2, return the empty string.
'''

str1 = input('Enter string: ')

if len(str1) > 2:
    str2 = str1[:2] + str1[-2:]
else:
    str2 = ""

print('String: ', str2)
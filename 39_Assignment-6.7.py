#   7. Write a Python program to check whether a string starts with specified characters.

str = input('Enter string: ')
ch = input('Enter specified character: ')

if str.endswith(ch):
    print(f"{str}, ends with {ch}.")
else:
    print(f"{str}, not ends with {ch}.")
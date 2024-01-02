# 1. Write a Python program to count the characters frequency in a string.

str = input('Enter the string: ')
ch = input("Enter character to check it's frequency: ")
count = 0

for i in str:
    if i == ch:
        count += 1

print(f"Frequency of {ch} in {str} is: {count}")
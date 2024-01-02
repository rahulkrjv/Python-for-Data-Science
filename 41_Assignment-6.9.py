#   9. Write a python program that to input a string and find and print the word having maximum length

str1 = input('Enter string: ')
lst = str1.split()

print(f"word having max length: {max(lst)}")
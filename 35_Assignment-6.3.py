''' 3. Write a Python program to get a string from a given string where all occurrences 
of that char have been changed to '$', except the first char.'''

str = input('Enter string: ')
ch = input('Enter character: ')
idx = str.find(ch)

temp = str[idx + 1:]
temp = temp.replace(ch, '$')
str = str[:idx + 1] + temp

print('New string: ', str)
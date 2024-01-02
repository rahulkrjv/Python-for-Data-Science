''' Write a program to convert days into years, weeks and days.'''

days = int(input('Enter no, of days: '))

months = days // 30
years = days // 365

print(f"{days} days = {months} months = {years} years")
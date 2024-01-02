''' Write a program to enter length in centimeter and convert it into meter and kilometer.'''

length = int(input('Enter the length (in cm): '))

print(f"{length} cm = {length / (10 ** 2)} m = {length / (10 ** 5)} km")
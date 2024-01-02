''' 4. Write a Python program to check whether the given number is Armstrong
or not.'''

num = (int(input('enter a number: ')))
temp = num; cubeOfDigits = 0

while(temp > 0):
    cubeOfDigits += (temp % 10) ** 3
    temp //= 10

if num == cubeOfDigits:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} isn't an Armstrong number.")
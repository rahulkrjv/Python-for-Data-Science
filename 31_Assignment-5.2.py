# WAP to check wheather the given number is handsome number or not.
    #   Handsome no. :- sum of left digits = last digit {For ex: 134 => 1 + 3 = 4}

import time

num = int(input('Enter the number: '))
sum = 0
last_digit = num % 10

while num > 0:
    num //= 10
    sum += num % 10

    if(sum > last_digit):
        print("Not Handsome no.")
        break

else:
    if(last_digit == sum):
        print("Handsome no.")
    else:
        print("Not Handsome no.")
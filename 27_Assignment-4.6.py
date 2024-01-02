# 6. Write a Python program to print first five Armstrong number starting from 10.

count = 0; num = 10

print ("First five Armstrong number starting from 10:")

while (count < 5):
    temp = num; sum = exp = 0

    while(temp > 0):
        temp //= 10
        exp += 1

    temp = num

    while(temp > 0):
        sum += (temp % 10) ** exp
        temp //= 10

    if num == sum:
        print(num, end = " ")
        count = count + 1
    num = num + 1
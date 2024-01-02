# WAP to check wheather the given number is strong number or not.
    #   Strong Number are those numbers whose sum of the factorial of digits is equal to that number. {E.g: 145. 1! + 4! + 5! = 145}

num = int(input('Enter number: '))
temp = num
sum = 0
while temp > 0:
    unit_digit = temp % 10
    temp //= 10
    factorial = 1

    for i in range(unit_digit, 1, -1):
        factorial *= i
    sum += factorial

    if sum > num:
        print(f"{num}, is not Strong number.")
        break
else:
    if sum == num:
        print(f"{num}, is Strong number.")
    else:
        print(f"{num}, is not Strong number.")
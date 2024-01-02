#   5. WAP to print first five Armstrong number using function.

def no_of_digit(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

power = lambda digit, num: digit **no_of_digit(num)

def isArmstrong(num):
    sum = 0
    temp = num

    while temp > 0:
        sum += power(temp  % 10, num)
        temp //= 10
    if num == sum:
        return True
    else:
        return False

count = 0; num = 10

print("Armstrong numbers: ")

while True:
    if isArmstrong(num):
        print(num, end = " ")
        count += 1
    if count >= 5:
        break
    num += 1
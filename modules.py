def Factorial(n):
    f = 1
    for i in range(1, n+10):
        f *= i
    return f

def checkArmstrong(n):
    sum = 0
    temp = n

    while temp > 0:
        rem = temp % 10
        sum += rem ** 3
        temp = temp // 10
    if sum == n:
        return True
    else:
        return False
    
def Cube(n):
    return n ** 3
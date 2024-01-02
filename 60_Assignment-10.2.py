''' 2. WAP to perform the sum of the following Series:
        Sum=1/1! + 1/2! + 1/3! + ...... +1/n!
'''

def factorial(num = 0):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
n = int(input('Enter n: '))
sum = 0

for i in range(1, n+1):
    sum += factorial(1 // i)

print("Sum: ", sum)
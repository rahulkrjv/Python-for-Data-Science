''' 3. WAP to perform the sum of the following Series:
        Sum=1^3+2^3 + 3^3 + ...... +n3'''

power = lambda num: num ** 3

n = int(input('Enter n: '))
sum = 0

for i in range(1, n+1):
    sum += power(i)
print("sum = ", sum)
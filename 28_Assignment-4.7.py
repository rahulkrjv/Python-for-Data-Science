# 7. WAP to check whether the given number is prime or not.

num = int(input('Enter a number: '))
'''
flag = True

for i in range(2, num // 2 + 1):
    if num % i == 0:
        flag = False
        break

if flag:
    print(f"{num}, is prime.")
else:
    print(f"{num}, is not prime.")
'''

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(f"{num}, is not prime.")
        break

else:
    print(f"{num}, is prime.")

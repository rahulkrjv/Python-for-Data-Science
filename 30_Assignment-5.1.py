'''
WAP to print the following patterns:
*                       *       * * * * *       * * * * *               *
* *                   * *       * * * *           * * * *             * * *
* * *               * * *       * * *               * * *           * * * * *
* * * *           * * * *       * *                   * *         * * * * * * *
* * * * *       * * * * *       *                       *       * * * * * * * * *

1               5 4 3 2 1       A               A B C D E
1 2             5 4 3 2         A B               A B C D
1 2 3           5 4 3           A B C               A B C
1 2 3 4         5 4             A B C D               A B
1 2 3 4 5       5               A B C D E               A
'''

print("\n---------- First Pattern ----------\n")

for i in range(5):
    for j in range(i + 1):
        print("*", end = " ")
    print()

print("\n---------- Second Pattern ----------\n")

for i in range(5):
    for j in range(5 - i):
        print(" ", end = " ")
    for j in range(i + 1):
        print("*", end = " ")
    print()
    
print("\n---------- Third Pattern ----------\n")

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()

print("\n---------- Fourth Pattern ----------\n")

for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end = " ")
    for j in range(i):
        print("*", end = " ")
    print()

print("\n---------- Fifth Pattern ----------\n")

for i in range(1, 10, +2):
    for j in range((9 - i) // 2 + 1):
        print(" ", end = " ")
    for j in range(i):
        print("*", end = " ")
    print()
    
print("\n---------- Sixth Pattern ----------\n")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()
    
print("\n---------- Seven Pattern ----------\n")

for i in range(5):
    for j in range(5, i, -1):
        print(j, end = " ")
    for j in range(5 - i):
        print("", end = " ")
    print()
    
print("\n---------- Eighth Pattern ----------\n")
temp = ord('A')
for i in range(temp, temp + 5):
    for j in range(temp, i + 1):
        print(chr(j), end = " ")
    print()
    
print("\n---------- Ninth Pattern ----------\n")

for i in range(temp, temp + 5):
    for j in range(i - temp):
        print(" ", end = " ")
    for j in range(temp, temp + (temp - i) + 5):
        print(chr(j), end = " ")
    print()
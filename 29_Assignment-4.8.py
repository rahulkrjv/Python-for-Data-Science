'''
8. Write a program to print following patterns.
*           *****       *               A
**          ****        **              A B
***         ***         ***             A B C
****        **          ****            A B C D
*****       *           *****           A B C D E
                        ******
                        *****
                        ****
                        ***
                        **
                        *
'''
print("1st pattern:\n-------------------------\n")

for i in range(0, 5):
    for i in range(i + 1, 0, -1):
        print("*", end = " ")
    print()

print("\n\n2nd pattern:\n-------------------------\n")

for i in range(5, 0, -1):
    for i in range(i, 0, -1):
        print("*", end = " ")
    print()

print("\n\n3rd pattern:\n-------------------------\n")

for i in range(0, 6):
    for i in range(i + 1, 0, -1):
        print("*", end = " ")
    print()
for i in range(5, 0, -1):
    for i in range(i, 0, -1):
        print("*", end = " ")
    print()

print("\n\n4th pattern:\n-------------------------\n")

temp = ord('A')

for i in range(temp, temp + 5):
    for j in range(temp, i + 1):
        print(chr(j), end = " ")
    print("")
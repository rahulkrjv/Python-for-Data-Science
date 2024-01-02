''' 2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
 2000 and 2100 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line. '''

print('Numbers divisible by 7 but not multiple of 5 between 2000-2100:')

for i in range(2000, 2100 + 1):
    if i % 7 == 0 and i % 5 != 0:
        if i == 2093:
            print(i, end = ".\n")
            continue
        print(i, end = ", ")        
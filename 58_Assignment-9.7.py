#   7. Write a Python program to remove the intersection of a 2nd set from the 1st set

set1 = set(input("Enter the set1: ").split(" "))
set2 = set(input("Enter the set2: ").split(" "))

set1 = set1 - set2

print(f"After removing, set1 is: {set1}")

'''
for i in set1.intersection(set2):
    set1.pop(i)
'''
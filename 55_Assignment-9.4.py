#   4. Write a Python program to check if two given sets have no elements in common.

set1 = set(input("Enter the set1: ").split(" "))
set2 = set(input("Enter the set2: ").split(" "))

if set1.isdisjoint(set2):
    print("No common elements.")
else:
    print("Have common elements.")
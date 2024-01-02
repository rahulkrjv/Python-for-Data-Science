#   6. Write a Python program to find the elements in a given set that are not in another set.

set1 = set(input("Enter the set1: ").split(" "))
set2 = set(input("Enter the set2: ").split(" "))

print(f"Elements that are in set1 only: {set1 - set2}")
#   5. Write a Python program to check if a given set is superset of itself and superset of another given set.

set1 = set(input("Enter the set1: ").split(" "))
set2 = set(input("Enter the set2: ").split(" "))

if set1.issuperset(set1):
    print("Given set is superset of itself.")
else:
    print("Hgiven set is not superset of itself.")

if set1.issuperset(set2):
    print("Given set is superset of set2.")
else:
    print("Hgiven set is not superset of set2.")
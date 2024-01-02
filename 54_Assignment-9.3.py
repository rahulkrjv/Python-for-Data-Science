#   3. Write a Python program to check if a given value is present in a set or not.

set1 = set(input("Enter the set: ").split(" "))
val = input("Enter the element to search: ")

if set1.issuperset({val}):
    print(f"{val} is present in set.")
else:
    print(f"{val} is not present in set.")
''' Write a Python program to swap two numbers. '''

a = input('Enter the value of A:\t')
b = input('Enter the value of B:\t')

# Python evaluates expressions from left to right (except when evaluating assignment).
# In an assignment statement, the right side is always evaluated fully before proceeding with the actual assignment of values to variables.

a , b = b , a

print(f"\nAfter swapping: \nA = {a} \t B = {b}")
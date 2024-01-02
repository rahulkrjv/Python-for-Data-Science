'''
6. Create a menu driven program to perform following task:
1. Addition
2. Subtraction
3. Multiply
4. Divide
'''

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

operator = input('''\n**********************************
1. Enter '+' for addition
2. Enter '-' for substraction
3. Enter '*' for multiplication
4. Enter '/' for division           ''')

if operator == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == '/':
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Error!")
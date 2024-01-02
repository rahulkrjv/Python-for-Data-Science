''' 4. WAP to compute the following expression
        Result=(x! +y!)/z!'''

def factorial(num = 0):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
x = int(input('Enter x: '))
y = int(input('Enter y: '))
z = int(input('Enter z: '))

print(f"(x! +y!)/z! : {(factorial(x) + factorial(y)) / factorial(z)}")
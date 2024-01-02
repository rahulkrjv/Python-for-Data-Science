'''
4. Write a python program to input electricity unit charges and calculate total electricity bill according to the given condition:
    For first 50 units Rs. 0.50/unit
    For next 100 units Rs. 0.75/unit
    For next 100 units Rs. 1.20/unit
    For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill if bill amount is greater than 1000.
'''

unit = int(input('Enter total unit consumed: '))
bill = 0

if unit > 0:
    if unit <= 50:
        bill = unit * 0.50
    elif unit <= 150:
        bill = 25 + ((unit - 50) * 0.75)    # Bill for first 50 unit equals to 25.
    elif unit <= 250:
        bill = 100 + ((unit - 150) * 1.20)  # Bill for first 150 unit equals to 100.
    else:
        bill = 220 + ((unit - 250) * 1.5)   # Bill for first 250 unit equals to 220.

if bill > 1000:
    bill += bill * 0.2

print(f"Your total bill is: Rs. {bill}")
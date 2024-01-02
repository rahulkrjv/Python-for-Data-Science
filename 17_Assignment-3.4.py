'''
4. Enter basic salary from the user. Write a program to calculate DA and HRA on the following conditions:-
Salary               DA     HRA
<=2000              10%     20%
>2000 && <=5000     20%     30%
>5000 && <=10000    30%     40%
>10000              50%     50%
'''

basic_salary = int(input('Enter your salary: '))

if basic_salary >= 0:
    if basic_salary <= 2000:
        salary = basic_salary + (basic_salary * (0.10 + 0.20))
    elif basic_salary <= 5000:
        salary = basic_salary + (basic_salary * (0.20 + 0.30))
    elif basic_salary <= 10000:
        salary = basic_salary + (basic_salary * (0.30 + 0.40))
    else:
        salary = basic_salary + (basic_salary * (0.50 + 0.50))
else:
    salary = 0

print(f"Gross salary = Rs. {salary}")
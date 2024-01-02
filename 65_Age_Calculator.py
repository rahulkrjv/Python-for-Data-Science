import datetime as dt

today = dt.date.today()
dob = input('Enter your DOB [YYYY-MM-DD]: ').split('-')
dob = [int(i) for i in dob]
dob = dt.date(dob[0], dob[1], dob[2])

age = (today - dob).days
print(f"\nAge: {age // 365} years, {(age % 365) // 30} months, {(age % 365) % 30} days\n")
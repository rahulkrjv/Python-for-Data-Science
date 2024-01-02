#  3. Write a python program to display a greet message according to the marks obtained by the student.

marks = float(input('Enter your marks: '))

if marks > 90 and marks <= 100:
    print("Congratulations! You have obtained 'O' grade.")
elif marks > 80:
    print("Congratulations! You have obtained 'A+' grade.")
elif marks > 70:
    print("Congratulations! You have obtained 'A' grade.")
elif marks > 60:
    print("Congratulations! You have obtained 'B+' grade.")
elif marks > 50:
    print("Congratulations! You have obtained 'B' grade.")
elif marks > 40:
    print("Congratulations! You have obtained 'C+' grade.")
elif marks >= 33.33:
    print("Congratulations! You have obtained 'C' grade.")
else:
    print("You have failed!")
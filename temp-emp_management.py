'''
Employee Management System
1. Insert Record
2. Edit Record
3. Display All Record
4. Display Record By Id
5. Delete a Record
6. Exit
In this application you mantain the following employee records eid, name, email, phone
'''

import os

def inputDetail():
    eId = int(input('Enter id no.: '))
    name = input('Enter Name: ')
    email = input('Enter Email: ')
    phone = int(input('Enter Phone: '))

    return (eId, name, email, phone)

employee = {}   #   employee = {'Eid' : [Name, Email, Phone]}

while True:
    key = int(input('''\n------- Employee Management System -------\n
Enter [1] to 'Insert Record'
Enter [2] to 'Edit Record'
Enter [3] to 'Display All Record'
Enter [4] to 'Display Record By Id'
Enter [5] to 'Delete a Record'
Enter [6] to 'Exit'\t\t   _'''))
    
    if key == 1:
        while True:
            value = inputDetail()
            file = open("employee.txt", "a")
            file.write(f"{value[0]} - {value[1]} - {value[2]} - {value[3]}\n")
            file.close()

            print("Successfully inserted the record.")

            temp = input('To continue enter [Y]: ')
            if temp == 'Y' or temp == 'y':
                print()
                continue
            else:
                break

    elif key == 2:
        flag = True
        eId = int(input('Enter the Eid: '))
        file = open("employee.txt", "r")
        tempFile = open("temp.txt", "w")

        for i in file.readlines():
            value = i.split("-")
            if int(value[0]) == eId:
                value = inputDetail()
                tempFile.write(f"{value[0]} - {value[1]} - {value[2]} - {value[3]}\n")
                flag = False
            else:
                tempFile.write(f"{value[0]} - {value[1]} - {value[2]} - {value[3]}\n")
        if flag:
            print("Id not matched!")

        file.close()
        tempFile.close()
        os.remove("employee.txt")
        os.rename("temp.txt", "employee.txt")

        print("Successfully edited the record.")

    elif key == 3:
        file = open("employee.txt", "r")

        print('''------------------------------------------------
Eid\t Name\t\t E-mail\t\t Phone
------------------------------------------------\n''')
        for i in file.readlines():
            print(f"{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}")
        file.close()

    elif key == 4:
        eId = int(input('Enter the Eid: '))
        file = open("employee.txt", "r")
        
        for i in file.readlines():
            value = i.split("-")
            if int(value[0]) == eId:
                print(f'''------------------------------------------------
Eid\t Name\t\t E-mail\t\t Phone
{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}
------------------------------------------------\n''')
        file.close()

    elif key == 5:
        flag = True
        eId = int(input('Enter the Eid: '))
        file = open("employee.txt", "r")
        tempFile = open("temp.txt", "w")

        for i in file.readlines():
            value = i.split("-")
            if int(value[0]) == eId:
                flag = False
                continue
            else:
                tempFile.write(f"{value[0]} - {value[1]} - {value[2]} - {value[3]}\n")
        if flag:
            print("Id not matched!")

        file.close()
        tempFile.close()
        os.remove("employee.txt")
        os.rename("temp.txt", "employee.txt")

        print("Successfully deleted the record.")         

    elif key == 6:
        print("Exiting...")
        break

    else:
        print("Can't understand. Please enter again.")
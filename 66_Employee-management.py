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
employee = {}   #   employee = {'Eid' : [Name, Email, Phone]}

def loadData():
    file = open("employee.txt", "r+")
    for i in file.readlines():
        if len(i) > 1:
            value = i.split(" - ")
            employee.update({int(value[0]): value[1:]})
    file.close()

def saveData():
    global employee
    file = open("temp.txt", "w")
    for i in employee:
        value = employee[i]
        file.write(f"{i} - {value[0]} - {value[1]} - {value[2]}\n")
    file.close()
    os.remove("employee.txt")
    os.rename("temp.txt", "employee.txt")

while True:
    key = int(input('''\n------- Employee Management System -------\n
Enter [1] to 'Insert Record'
Enter [2] to 'Edit Record'
Enter [3] to 'Display All Record'
Enter [4] to 'Display Record By Id'
Enter [5] to 'Delete a Record'
Enter [6] to 'Exit'\t\t   _'''))
    
    if key == 1:
        employee.clear()
        loadData()
        while True:
            eId = int(input('Enter id no.: '))
            name = input('Enter Name: ')
            email = input('Enter Email: ')
            phone = int(input('Enter Phone: '))
            length = len(employee)

            employee.update({eId : [name, email, phone]})

            if len(employee) > length:
                print("Successfully inserted the record.")
                temp = input('To continue enter [Y]: ')

                if temp == 'Y' or temp == 'y':
                    print()
                    continue
                else:
                    break
            else:
                print('Error! Please enter again.')
        saveData()

    elif key == 2:
        employee.clear()
        loadData()
        eId = int(input('Enter the Eid: '))

        for i in employee:
            if i == eId:
                name = input('Enter Name: ')
                email = input('Enter Email: ')
                phone = int(input('Enter Phone: '))
                length = len(employee)

                employee.update({eId : [name, email, phone]})

                if len(employee) == length:
                    print("Successfully edited the record.")
                else:
                    print('Error! Please enter again.')
                break
        else:
            print("Id not matched!")
        saveData()

    elif key == 3:
        employee.clear()
        loadData()
        print('''------------------------------------------------
Eid\t Name\t\t E-mail\t\t Phone
------------------------------------------------\n''')
        for i in employee.items():
            #temp = employee.get(key)
            print(f"{i[0]}\t{i[1][0]}\t{i[1][1]}\t{i[1][2]}")
        
        saveData()

    elif key == 4:
        employee.clear()
        loadData()
        eId = int(input('Enter the Eid: '))
        temp = employee.get(eId)
        
        print(f'''------------------------------------------------
Eid\t Name\t\t E-mail\t\t Phone
{eId}\t{temp[0]}\t{temp[1]}\t{temp[2]}
------------------------------------------------\n''')
        
        saveData()

    elif key == 5:
        employee.clear()
        loadData()
        eId = int(input('Enter the Eid: '))
        
        for i in employee:
            if i == eId:
                length = len(employee)

                employee.pop(eId)

                if len(employee) < length:
                    print("Successfully inserted the record.")
                else:
                    print('Error! Please enter again.')
                break
        else:
            print("Id not matched!")

        saveData()     

    elif key == 6:
        print("Exiting...")
        break

    else:
        print("Can't understand. Please enter again.")
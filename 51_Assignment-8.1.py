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

    elif key == 2:
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

    elif key == 3:
        print('''------------------------------------------------
Eid\t Name\t\t E-mail\t\t Phone
------------------------------------------------\n''')
        for i in employee.items():
            #temp = employee.get(key)
            print(f"{i[0]}\t{i[1][0]}\t{i[1][1]}\t{i[1][2]}")

    elif key == 4:
        eId = int(input('Enter the Eid: '))
        temp = employee.get(eId)
        
        print(f'''------------------------------------------------
Eid\t Name\t\t E-mail\t\t Phone
{eId}\t{temp[0]}\t{temp[1]}\t{temp[2]}
------------------------------------------------\n''')

    elif key == 5:
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

    elif key == 6:
        print("Exiting...")
        break

    else:
        print("Can't understand. Please enter again.")
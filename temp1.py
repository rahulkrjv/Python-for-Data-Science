def EditRecord():
    id = int(input("Enter Student Id : "))
    cursor.execute("select * from studentinfo where sid="+str(id))
    result = cursor.fetchall()
    if len(result) > 0:
        while True:
            print ("Enter 1 to update name")
            print("Enter 2 to update email id")
            print ("Enter 3 to update Date of Birth")
            print ("Enter 4 to update conatct detail")
            print ("Enter 5 to update address")
            print("Enter 6 to update All")
            print ("Enter 7 to Back")
            ch = int(input("Enter Choice: "))
            if ch == 1 :
                name = input("Enter Name : ")
                cursor.execute("update studentinfo set name='"+name+"' where sid = "+str(id))
                con.commit()
                if cursor.rowcount>0:
                    print("Record updated successfully.")
                else:
                    print("Error in updating the record!")
            elif ch == 2:
                email = input("Enter Email : ")
                cursor.execute(f"update studentinfo set Email ='{email}' where sid = {id}")
                con.commit()
                if cursor.rowcount>0:
                    print("Record updated successfully.")
                else:
                    print("Error in updating the record!")

            elif ch == 3:
                dob = input("Enter DOB(YYYY-MM-DD) : ")
                cursor.execute(f"update studentinfo set DOB ='{dob}' where sid = {id}")
                con.commit()
                if cursor.rowcount>0:
                    print("Record updated successfully.")
                else:
                    print("Error in updating the record!")

            elif ch == 4:
                contact = int(input("Enter Contact : "))
                cursor.execute(f"update studentinfo set Contact ={contact} where sid = {id}")
                con.commit()
                if cursor.rowcount>0:
                    print("Record updated successfully.")
                else:
                    print("Error in updating the record!")

            elif ch == 5:
                add = input("Enter Address : ")
                cursor.execute(f"update studentinfo set Address ='{add}' where sid = {id}")
                con.commit()
                if cursor.rowcount>0:
                    print("Record updated successfully.")
                else:
                    print("Error in updating the record!")

            elif ch == 6:
                name = input("Enter Name : ")
                email = input("Enter Name : ")
                dob = input("Enter DOB(YYYY-MM-DD) : ")
                contact = int(input("Enter Contact : "))
                add = input("Enter Address : ")
                cursor.execute(f"update studentinfo set Name = '{name}', Email = '{email}',DOB = '{dob}', Contact = {contact}, Address = '{add}' where sid = {id}")
                con.commit()
                if cursor.rowcount>0:
                    print("Record updated successfully.")
                else:
                    print("Error in updating the record!")

            elif ch == 7:
                break
            else:
                print("Invalid input.")
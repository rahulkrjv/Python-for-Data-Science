''' 1. Define a class named Employee with the following fields: empID, empName, deptID, bloodGroup, salary.
    Declare and define following methods :
        setEmployee Details(), printEmployeeDetails()
        WAP to read and display the record of N employee.'''

class Employee:
    def __init__(self):
        empID = ""
        empName = ""
        deptID = ""
        bloodGroup = ""
        salary = 0.0
    def setEmployeeDetails(self):
        self.empId = input("Enter Employee Id: ")
        self.empName = input("Enter Employee Name: ")
        self.deptID = input("Enter Department Id: ")
        self.bloodGroup = input("Enter Employee's Bloodgroup: ")
        self.salary = float(input("Enter Employee's Salary: "))
    def printEmployeeDetails(self):
        print("%5s \t %20s \t %4s \t\t %2s \t %7.2f" %(self.empId, self.empName, self.deptID, self.bloodGroup, self.salary))

lst = []
n = int(input("Enter no. of employees: "))

for i in range(n):
    emp = Employee()
    emp.setEmployeeDetails()
    lst.append(emp)

print("%5s \t %20s \t %4s \t %2s \t %7s" %('Emp Id', 'Name', 'DeptID', 'BGrp', 'Salary'))
for i in lst:
    i.printEmployeeDetails()
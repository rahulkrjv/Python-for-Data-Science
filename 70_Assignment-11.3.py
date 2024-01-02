''' 3. Define a class to represent a bank account which include the following
members as:
Data members:
    1. Name of the depositor
    2. Account Number
    3. Withdraw amount
    4. Balance amount in the account
Member Functions:
    1. To assign initial values
    2. To deposit an amount
    3. To withdraw an amount after checking the balance
    4. To display name and balance.
Write a main program to test the program.'''

class Account:
    def __init__(self):
        name = input("Enter your Name: ")
        acNo = input("Enter Ac No.: ")
        balance = float(input("Enter Balance: "))
    def deposit(self):
        self.balance += float(input("Enter the amount to deposit: "))
    def withdraw(self):
        amt = float(input("Enter the amount to deposit: "))
        if amt <= self.balance:
            self.balance -= amt
            print("Successfully withdrew.")
        else:
            print("Insufficient nalance.")
    def display(self):
        print('''\n******************************
Name: {self.name}
Account Number: {self.acNo}
Balance: {self.balance}\n''')
        
def menu():
    return int(input('''------------------------------------
1. Create account
2. Deposit
3. Withdraw
4. Details
5. Exit'''))

lst = []
while True:
    key = menu()
    if key == 1:
        acc = Account()
        lst.append(acc)
    elif key == 2:
        acNo = input("Enter Ac No.: ")
        for i in lst:
            if i.acNo == acNo:
                i.deposit()
                break
        else:
            print("Account not found.")
    elif key == 3:
        acNo = input("Enter Ac No.: ")
        for i in lst:
            if i.acNo == acNo:
                i.withdraw()
                break
    elif key == 4:
        break
    else:
        print("Invalid input.")
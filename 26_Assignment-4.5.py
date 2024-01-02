# 5. Write a Python program to get the Fibonacci series between 0 to 50.

temp1 = 0; temp2 = 1

print("Fibonacci serries (0-50):")
print(f"{temp1}, {temp2}", end = ", ")

for i in range(0, 50):
    if i == (temp1 + temp2):
        print(i, end = ", ")
        temp1 = temp2
        temp2 = i
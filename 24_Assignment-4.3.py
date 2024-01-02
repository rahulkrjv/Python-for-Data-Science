''' 3. A number is input through the keyboard. Write a program to obtain the reversed
 number and to determine whether the original and reversed number is equal or not (palindrome).'''

num = (int(input('enter a number: ')))
temp = num; reverse = 0

while(temp > 0):
    reverse = (reverse * 10) + (temp % 10)
    temp //= 10

print(f"Reverse of {num} = {reverse}")

if num == reverse:
    print("it's a 'palindrome'.")
else:
    print("it isn't a 'palindrome'.")
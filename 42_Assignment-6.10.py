#   10. Write a python program that to input a string and find a max length palindrome substring within it and display.


#   sir i tried this way, but there was some problem
str = input('Enter string: ')
palindrome = ''
x = 0

for i in str:
    y = len(str) -1
    for j in str[-1:x - 1 + 1:-1]:
        if i == j:
            temp = str[x:y + 1]
            print(temp)
            if x == y:
                break
        else:
            y -= 1
            continue

        if temp == temp[-1::-1]:
            if len(temp) > len(palindrome):
                palindrome = temp
        y -= 1
    x += 1

print('palindrome substring: ', palindrome)



# 7. WAP to check whether the input character is vowel or not.

char = input('Enter an alphabet: ')
vowel = 'AEIOUaeiou'

if char in vowel:
    print("It is a vowel.")
else:
    print("It is a constant.")
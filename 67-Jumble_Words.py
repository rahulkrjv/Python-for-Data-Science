import os
import random

def loadData(fileName):
    file = open(fileName, "r")
    temp = file.read().split(" ")
    file.close()

    return tuple(temp)

def display(mode):
    val = random.choice(mode)
    temp = ''.join(random.sample(val, len(val)))
    print("Guess the word:", temp)
    user = input()
    return (val, user)

def menu():
    key = int(input(f'''*************************\n
1. Easy Mode
2. Standard Mode
3. Hard Mode
4. Exit             '''))
    return key

easy = loadData("easy.txt")
std = loadData("standard.txt")
hard = loadData("hard.txt")

while True:
    key = menu()

    if key == 1:
        print("****** Easy Mode ******\n")
        for i in range(10):
            try:
                value = display(easy)
            except:
                print("Invalid Input.")
                break
            else:
                if value[0] == value[1]:
                    print("Correct answer!")
                else:
                    print("Incorrect answer. You lost")
                    break
        else:
            print("Congratulations! You won...")

    elif key == 2:
        print("****** Standard Mode ******\n")
        for i in range(10):
            try:
                value = display(std)
            except:
                print("Invalid Input.")
                break
            else:
                if value[0] == value[1]:
                    print("Correct answer!")
                else:
                    print("Incorrect answer. You lost")
                    break
        else:
            print("Congratulations! You won...")

    elif key == 3:
        print("****** Hard Mode ******\n")
        for i in range(10):
            try:
                value = display(hard)
            except:
                print("Invalid Input.")
                break
            else:
                if value[0] == value[1]:
                    print("Correct answer!")
                else:
                    print("Incorrect answer. You lost")
                    break
        else:
            print("Congratulations! You won...")

    elif key == 4:
        os._exit()

    else:
        print("Invalid input!")
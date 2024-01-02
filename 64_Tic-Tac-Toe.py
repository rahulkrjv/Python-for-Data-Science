lst = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def winner():
    for i in range(0, 3):
        key = True
        for j in range(0, 3):
            if lst[i][0] != lst[i][j]:
                key = False
        if key == True:
            return [True, lst[i][0]]
        
    for i in range(0, 3):
        key = True
        for j in range(0, 3):
            if lst[0][i] != lst[j][i]:
                key = False
        if key == True:
            return [True, lst[0][i]]
        
    key = True
    for i in range(0, 3):
        if lst[0][0] != lst[i][i]:
            key = False
    if key == True:
        return [True, lst[0][0]]
    
    key = True
    count1 = 0
    for i in range(0, 3):
        count2 = 0
        for j in range(2,-1,-1):
            if count1 == count2:
                if lst[1][1] != lst[i][j]:
                    key = False
            count2 += 1
        count1 += 1
    if key == True:
        return [True, lst[1][1]]
    else:
        return [False, []]

def table():
    print("=============")
    for i in range(0, 3):
        print("|", end= "")
        for j in range(0, 3):
            print("", lst[i][j], "|", end = "")
        print("\n=============")

turn = 1
table()
while turn < 10:

    if turn % 2 != 0:
        print("Player1's turn[O]: \nEnter your location")
        x = int(input("Enter row: "))
        y = int(input("Enter column: "))
        if lst[x][y] == '-':
            print(x, y)
            lst[x][y] = 'O'
        else:
            print("\nUnexpected Error!\n")
            continue
        print()

    else:
        print("Player2's turn[X]: \nEnter your location")
        x = int(input("Enter row: "))
        y = int(input("Enter column: "))

        if lst[x][y] == '-':
            print(x, y)
            lst[x][y] = 'X'
        else:
            print("\nUnexpected Error!\n")
            continue
        print()

    table()
    player = winner()

    if player[0]:
        if player[1] != '-':
            if player[1] == 'O':
                print(f"Winner: Player 1[O] (Round: {turn})")
            else:
                print(f"Winner: Player 2[X] (Round: {turn})")
            break
    turn += 1
else:
    print("Draw!")
ROW1 = [1,2,3]
ROW2 = [4,5,6]
ROW3 = [7,8,9]
def xTurn():
    print(ROW1)
    print(ROW2)
    print(ROW3)
    num = int(input("Choose a number: "))
    if (num == 1):
        ROW1[0] = "X"
    elif (num == 2):
        ROW1[1] = "X"
    elif (num == 3):
        ROW1[2] = "X"
    elif (num == 4):
        ROW2[0] = "X"
    elif (num == 5):
        ROW2[1] = "X"
    elif (num == 6):
        ROW2[2] = "X"
    elif (num == 7):
        ROW3[0] = "X"
    elif (num == 8):
        ROW3[1] = "X"
    elif (num == 9):
        ROW3[2] = "X"

def oTurn():
    print(ROW1)
    print(ROW2)
    print(ROW3)
    num = int(input("Choose a number: "))
    if (num == 1):
        ROW1[0] = "O"
    elif (num == 2):
        ROW1[1] = "O"
    elif (num == 3):
        ROW1[2] = "O"
    elif (num == 4):
        ROW2[0] = "O"
    elif (num == 5):
        ROW2[1] = "O"
    elif (num == 6):
        ROW2[2] = "O"
    elif (num == 7):
        ROW3[0] = "O"
    elif (num == 8):
        ROW3[1] = "O"
    elif (num == 9):
        ROW3[2] = "O"
def winCheckOs():
    if(ROW1[0]== "O" and ROW2[0] == "O" & ROW3[0] == "O"):
        return True
    if(ROW1[1]== "O" and  ROW2[1] == "O" and ROW3[1] == "O"):
        return True
    if(ROW1[2]== "O" and  ROW2[2] == "O" and ROW3[2] == "O"):
        return True
    if(ROW1[0]== "O" and  ROW1[1] == "O" and ROW1[2] == "O"):
        return True
    if(ROW2[0]== "O" and  ROW2[1] == "O" and ROW2[2] == "O"):
        return True
    if(ROW3[0]== "O" and  ROW3[1] == "O" and ROW3[2] == "O"):
        return True
    if(ROW1[0]== "O" and  ROW2[1] == "O" and ROW3[2] == "O"):
        return True
    if(ROW1[2]== "O" and  ROW2[1] == "O" and ROW3[0] == "O"):
        return True
def winCheckXs():
    if (ROW1[0] == "X" and ROW2[0] == "X" and ROW3[0] == "X"):
        return True
    if (ROW1[1] == "X" and ROW2[1] == "X" and ROW3[1] == "X"):
        return True
    if (ROW1[2] == "X" and ROW2[2] == "X" and ROW3[2] == "X"):
        return True
    if (ROW1[0] == "X" and ROW1[1] == "X" and ROW1[2] == "X"):
        return True
    if (ROW2[0] == "X" and ROW2[1] == "X" and ROW2[2] == "X"):
        return True
    if (ROW3[0] == "X" and ROW3[1] == "X" and ROW3[2] == "X"):
        return True
    if (ROW1[0] == "X" and ROW2[1] == "X" and ROW3[2] == "X"):
        return True
    if (ROW1[2] == "X" and ROW2[1] == "X" and ROW3[0] == "X"):
        return True

if __name__ == '__main__':
    print("Hello welcome to Tik Tac Toe")
    rounds = 1
    while(rounds <= 5):
        print("Round: ", rounds)
        print("X's turn")
        xTurn()
        if(winCheckXs() == True):
            print("X's win")
            break
        print("O's turn")
        oTurn()
        rounds += 1
        if (winCheckOs() == True):
            print("0's win")
            break





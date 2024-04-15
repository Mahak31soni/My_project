def sum(a,b,c):
    return a+b+c

def printBoard(xState, zState):

    print(f"{'X' if xState[0] else ('O' if zState[0] else 0)} | {'X' if xState[1] else ('O' if zState[1] else 1)} | {'X' if xState[2] else ('O' if zState[2] else 2)} ")
    print(f"--|---|---")
    print(f"{'X' if xState[3] else ('O' if zState[3] else 3)} | {'X' if xState[4] else ('O' if zState[4] else 4)} | {'X' if xState[5] else ('O' if zState[5] else 5)} ")
    print(f"--|---|---")
    print(f"{'X' if xState[6] else ('O' if zState[6] else 6)} | {'X' if xState[7] else ('O' if zState[7] else 7)} | {'X' if xState[8] else ('O' if zState[8] else 8)} ")

    pass

def checkWin(xState, zState):

    Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in Wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the Match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the Match")
            return 0
            
    return -1

if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn = 1 #1 for x and 0 for o

    print("Welcome to Tic Tac Toe")
    steps = 0
    while True and steps < 9:

        printBoard(xState, zState)
        if turn == 1:
            print("X's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1
            turn = 0
        else:
            print("o's Chance")
            value = int(input("Please enter a value: "))
            zState[value] = 1
            turn  = 1
        cWin = checkWin(xState, zState)
        if(cWin != -1):
            print("Match Over")
            break
        steps = steps + 1
        if(cWin == -1):
            print(cWin, "Draw")



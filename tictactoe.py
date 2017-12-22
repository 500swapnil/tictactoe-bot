import random
import os
import time

os.system("clear")

board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]
turn = 1

def printBoard(board):
    print('-------------')
    for i in range(3):
        print('|',board[i][0],'|',board[i][1],'|',board[i][2],'|')
        print('-------------')

def play(board,turn,auto=False):
    if auto:
        print("My turn to play","X" if turn == 1 else "O")
        time.sleep(1)
        (a,b) = autoplay(board,turn)
        a -= 1
        b -= 1
    else:
        if turn == 1:
            inp = input("Choose the row and column to play X in: ").split()
        else:
            inp = input("Choose the row and column to play O in: ").split()
        if len(inp) != 2:
            print('Invalid move')
            play(board,turn)
            return

        if inp[0].isdigit() == False or inp[1].isdigit() == False:
            print('Invalid move')
            play(board,turn)
            return 

        if int(inp[0])>3 or int(inp[1])>3 or int(inp[1])<1 or int(inp[0])<1:
            print('Invalid move')
            play(board,turn)
            return

        a = int(inp[0]) - 1
        b = int(inp[1]) - 1
        if board[a][b] != ' ':
            print('Invalid move')
            play(board,turn)
            return
    if turn == 1:
        board[a][b] = 'X'
    else:
        board[a][b] = 'O'

def check(b):
    if (b[0][0] == b[0][1] and b[0][1] == b[0][2]) or (b[0][0] == b[1][0] and b[1][0] == b[2][0]) or (b[0][0] == b[1][1] and b[1][1] == b[2][2]):
        if b[0][0] == 'X':
            return 1
        elif b[0][0] == 'O':
            return 0
    if (b[1][1] == b[1][0] and b[1][1] == b[1][2]) or (b[1][1] == b[0][1] and b[1][1] == b[2][1]) or (b[1][1] == b[0][2] and b[1][1] == b[2][0]):
        if b[1][1] == 'X':
            return 1
        elif b[1][1] == 'O':
            return 0
    if (b[2][2] == b[2][1] and b[2][1] == b[2][0]) or (b[2][2] == b[1][2] and b[2][2] == b[0][2]):
        if b[2][2] == 'X':
            return 1
        elif b[2][2] == 'O':
            return 0
    return 2

def autoplay(board,turn):
    bestVal = -100
    bestMove = [0,2]
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X' if turn==1 else 'O'
                move = minimax(board,False,0,turn)
                if bestVal < move:
                    bestMove = [i,j]
                    bestVal = move
                board[i][j] = ' '
    bestMove[0] += 1
    bestMove[1] += 1
    return bestMove
                
def minimax(board,ismax,depth,turn):
    if check(board) != 2:
        if check(board) == turn:
            return 10 - depth
        else:
            return -10 + depth
    
    if ismax:
        best = -100
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X' if turn==1 else 'O'
                    best = max(best,minimax(board,False,depth+1,turn))
                    board[i][j] = ' '
        if best == -100:
            return 0
        return best
    
    else:
        best = 100
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X' if turn==0 else 'O'
                    best = min(best,minimax(board,True,depth+1,turn))
                    board[i][j] = ' '
        if best == 100:
            return 0
        return best

print("Welcome to TicTacToe\nEnter your name or 'AI' as the player name to make it a bot!\n\nHow to play?\n\nEnter the row and column of where you want to place your X or O"+
"\n\nExample\n"+
"-------------\n|   | X |   |\n"+
"-------------\n|   |   |   |\n"+
"-------------\n|   |   |   |\n"+
"-------------\n\n"+
"1 2\nThis move is played in the first row and second column\n\nPress Ctrl+C anytime to quit\n\n")
p1 = input("Enter player 1 name: ")
p2 = input("Enter player 2 name: ")

if p1 == "":
    p1 = "Player1"
if p2 == "":
    p2 = "Player2"

c = 0

while True:
    os.system("clear")
    printBoard(board)
    if check(board) == 1:
        print(p1,"wins")
        break
    elif check(board) == 0:
        print(p2,"wins")
        break
    if c == 9:
        print("Draw")
        break
    if (turn == 0 and p2 == "AI") or (turn == 1 and p1 == "AI"):
        play(board,turn,auto=True)
    else:
        if turn == 0:
            print(p2, "It's your turn!")
        else:
            print(p1, "It's your turn!")
        play(board,turn)
    c+=1
    turn = (turn+1)%2

'''things to addd
-play again feature
-second ship

-ships bigger than 1 space
    -more turns.. bigger board?.. 

-let user pick amount of ships 

'''
from random import randint

#initialize board
board = []
for n in range(5):
    board.append(["0"] * 5)

#define functions
def print_board(board):
    for n in board:
        print ' '.join(n)

def rand_row(board):
    rand_row = randint(0,len(board) - 1)
    return rand_row

def rand_col(board):
    rand_col = randint(0,len(board) - 1)
    return rand_col

#Generates random coordinates
ship1_row = int(rand_row(board))
ship1_col = int(rand_col(board))



#Running logic
for turn in range(4): 
    #Ask user to guess
    print "ship row " + str(ship1_row)
    print "ship row " + str(ship1_col)

   # guess_row = int(raw_input("Guess Row:"))
   # guess_col = int(raw_input("Guess Col:"))
   
    guess_row = ship1_row
    guess_col = ship1_col

    if guess_row == ship1_row and guess_col == ship1_col:
        print "It's a hit You win!"
        board[ship1_row][ship1_col] = "X"
        print_board(board)
        break
    else:
        if turn != 4:
            print "Miss"
            board[guess_row][guess_col] = "*"
            print_board(board)
        else:
            print "Game over"
            print "Here is where my ship was!"
            board[ship1_row][ship1_col] = "X"
            print_board(board)
print turn, turn + 1

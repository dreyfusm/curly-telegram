from random import randint

board = []

for n in range(5):
    board.append(["0"] * 5)

def print_board(board):
    for n in board:
        print ' '.join(n)

#print_board(board)

def rand_row(board):
    rand_row = randint(0,len(board) - 1)
    return rand_row
def rand_col(board):
    rand_col = randint(0,len(board) - 1)
    return rand_col

ship_row = rand_row(board)

ship_col =  rand_col(board)

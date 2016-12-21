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

#Generates random coordinates
ship_row = int(rand_row(board))
ship_col = int(rand_col(board))

#Ask user to guess
print "ship row " + str(ship_row)
print "ship row " + str(ship_col)

guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

if guess_row == ship_row and guess_col == ship_col:
    print "It's a hit"
    board[ship_row][ship_col] = "X"
    print_board(board)

else:
    print "Miss"
    board[guess_row][guess_col] = "*"
    print_board(board)

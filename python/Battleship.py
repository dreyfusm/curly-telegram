#things to add
##-play again feature
##  -- done by a while loop == check to see if play_again is still yes.. if changes, break loop and end
##  -- reset function to reset board and select new coords
##-second ship
## -ships bigger than 1 space
## -more turns.. bigger board?..
## -let user pick amount of ships
from random import randint
import sys

#initialize board

def create_board():
    """creates board"""
    newboard = []
    for n in range(5):
        newboard.append(["0"] * 5)
    return newboard

#define functions
def print_board(board):
    """prints board"""
    for n in board:
        print ' '.join(n)

def rand_row(board1):
    """creates random row number"""
    random_row = randint(1, len(board1) - 1)
    return random_row

def rand_col(board2):
    """creates random column number"""
    rand_column = randint(1, len(board2) - 1)
    return rand_column

print ""
print ""
print "Welcome to Battle Ship. If you can guess where my ship is in four turns, you win!"
print ""
print ""


#Running logic

playagain = 'yes'
while playagain == 'yes':
    print "debug"
    board = create_board()
    ship1_row = int(rand_row(board))
    ship1_col = int(rand_col(board))
    print_board(board)
    for turn in range(4):
        #Ask user to guess
        print ""
        print "ship row " + str(ship1_row)
        print "ship row " + str(ship1_col)
        print "You have " + str((range(4)[3] + 1) - turn) + " turns left."
        print "~~~~~~~~~~~~~~"
        while True:
            try:
                guess_row = -3
                while guess_row < 1 or guess_row > 5:
                    try:
                        guess_row = int(raw_input("Guess Row:"))
                        if guess_row < 1 or guess_row > 5:
                            print "Invalid input"
                        else:
                            break
                    except ValueError:
                        print "Input not valid"
                guess_col = -3
                while guess_col < 1 or guess_col > 5:
                    try:
                        guess_col = int(raw_input("Guess Col:"))
                        if guess_col < 1 or guess_col > 5:
                            print "Invalid input"
                        else:
                            break
                    except ValueError:
                        print "Input not valid"
            except ValueError:
                print "Not a valid input."
            break
        #Need to validate inputs (out of range inputs and letters)
        print "~~~~~~~~~~~~~~"

        if guess_row == ship1_row and guess_col == ship1_col:
            print "It's a hit You win!"
            board[ship1_row - 1][ship1_col - 1] = "X"
            print_board(board)
            #ask user if they want to play again
            response = raw_input("Would you like to play again?")
            playagain = response
            break
        else: #continue game
            if turn != 4:
                print "Miss!"
                print "~~~~~~~~~~~~~~"
                if guess_col == 0:
                    board[guess_row - 1][guess_col] = "*"
                elif guess_row == 0:
                    board[guess_row][guess_col - 1] = "*"
                elif guess_col == 0 and guess_row == 0:
                    board[guess_row][guess_col] = "*"
                else:
                    board[guess_row - 1][guess_col - 1] = "*"
                print_board(board)
                print "~~~~~~~~~~~~~~"
            else: #end game
                print "~~~~~~~~~~~~~~"
                print "Game over"
                print "Here is where my ship was!"
                board[ship1_row][ship1_col] = "X"
                print "~~~~~~~~~~~~~~"
                print_board(board)
print "Thanks for playing"

#things to add
##-play again feature
##-second ship
## -ships bigger than 1 space
## -more turns.. bigger board?..
## -let user pick amount of ships
from random import randint
import sys
#initialize board

def create_board():
    board = []
    for n in range(5):
        board.append(["0"] * 5)
    return board
#define functions
def print_board(board):
    for n in board:
        print ' '.join(n)

def rand_row(board1):
    rand_row = randint(0,len(board1) - 1)
    return rand_row

def rand_col(board2):
    rand_col = randint(0,len(board2) - 1)
    return rand_col

#left off here
def play_again(input):
    if play_again == "Y" or play_again == "Yes":
        return True
    elif play_again == "N" or play_again == "No":
        return True
    else:
        return False

#Generates random coordinates
board = create_board()
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
        #ask user if they want to play again
        while True:
            try: #validate
                response = raw_input("Would you like to play again? (Y or N)")
                str(response.upper())
                if isinstance(response, str) and response is "YES" or response is "NO" \
                or response is "N" or response is "Y" or response is "y" or response is "n"\
                or response is "yes" or response is "no": #circle back to clean up. figure out case insenstive conparsion
                    break
                else:
                #we're happy with the value given.
                #we're ready to exit the loop.
                    print "Please choose Y or N."
                    continue
            except ValueError:
                print "You broke it"
                sys.exit("womp womp")
        if response == "N" or response == "No" or response == "n" or response == "no":
            sys.exit("Thanks for playing!") #tested
        elif response == "Y" or response == "Yes" or response == "y" or response == "yes":
            print "invoke play_again method" #Debug
            play_again(response)
        else:
            print "Invalid response"
    else: #continue game
        if turn != 4:
            print "Miss"
            board[guess_row][guess_col] = "*"
            print_board(board)
        else:
            print "Game over"
            print "Here is where my ship was!"
            board[ship1_row][ship1_col] = "X"
            print_board(board)
turn + 1

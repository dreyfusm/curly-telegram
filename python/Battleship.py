#left off
#validation for computer mode

#In progress
#two player/computermode

#things to add
##-second ship
##- two player
## -ships bigger than 1 space
## -more turns.. bigger board?..
## -let user pick amount of ships

from random import randint

#Functions

def create_board():
    """creates board"""
    newboard = []
    for num in range(5):
        newboard.append(["0"] * 5)
    return newboard

def print_board(tboard):
    """prints board"""
    for num in tboard:
        print ' '.join(num)

def rand_row(board1):
    """creates random row number"""
    random_row = randint(1, len(board1) - 1)
    return random_row

def rand_col(board2):
    """creates random column number"""
    rand_column = randint(1, len(board2) - 1)
    return rand_column

def guess_validate(num):
    if num < 1 or num > 5:
        return False
    else:
        return True

def guess_validate_nums(row, col):
    if row < 1 or row > 5 and col < 1 or col > 5:
        return False
    else:
        return True

def duplicate_validate(row, col):
    if board[row - 1][col - 1] == "*":
        return False
    else:
        return True

def mark_board(row,col,symbol):
    board[row - 1][col - 1] = symbol
    return True

print ""
print ""
print "Welcome to Battle Ship. Object of the game is to guess where your opponent's ship is"
print ""
print "You have the option of playing against by yourself, against a computer, or a friend/enemy."


#Running logic to play against a computer.
playerinput = raw_input("So what will it be? ( self, computer or friend)")
playerinputval = playerinput
while playerinputval.lower() not in {'computer', 'self', 'friend'}:  # Fill in the condition (before the colon)
    playerinputval = raw_input("Don't think you can play against a " + playerinput)
if playerinputval == "friend": #play against friend
    #breakout code for two player
    print "filler "

elif playerinputval == "computer": #play against computer
#Things to implement for two player 
#player needs to choose a location on the board
#computer must have a turn (generate a random space)

    print "Gonna play against me aye? Well before we begin"
    print "here are the rules."
    print "Below is your board. Your ship is marked as an \"@\""
    print "Misses will be marked as \"*\""
    print "If you get lucky and hit my ship it'll mark as an \"X\""
    play_again = 'yes'
    while play_again == 'yes':
        print "To start, pick your coordinates. I wont peek!"
        board = create_board()
        print_board(board)
        check = False
        while check is False:
            player_row = int(raw_input("Select a row for your boat (1-5):"))
            player_col = int(raw_input("Select a col for your boat (1-5)"))
            if guess_validate_nums(player_row, player_col) is True and duplicate_validate(player_row, player_col) is True:
                check = True
        print "I marked you as the @ on the board. Remember, this is NOT a miss marker."
        mark_board(player_row, player_col, "@")
        print_board(board)
        ship1_row = int(rand_row(board))
        ship1_col = int(rand_col(board))
        print ship1_row
        print ship1_col
        hit = False
        while hit is False:                        ##################
            #player chooses space to guess..       #BEGIN VALIDATION#
            while True: #This while loop askes for user input. Validates it's an integer between 1 and 5
                try:    #and makes sure it's not a coordinate they already guessed
                    guess_row = -3
                    while guess_row < 1 or guess_row > 5:
                        try:
                            guess_row = int(raw_input("Guess Row:")) #get input
                            if guess_validate(guess_row) is False: #check to make sure it's in range
                                print "Invalid input"
                            else:
                                print "row validation passed"
                                break
                        except ValueError:
                            print "Input not valid"
                    guess_col = -3
                    while guess_col < 1 or guess_col > 5:
                        try:
                            guess_col = int(raw_input("Guess Col:"))
                            #guess_col = 3
                            if guess_validate(guess_col) is False:
                                print "Invalid input"
                            else:
                                print "pass col validation"
                                break
                        except ValueError:
                            print "Input not valid"
                    if duplicate_validate(guess_row, guess_col) is False: #check to make sure it's not already guessed
                        print "You've already guessed this coordinate!"
                    else:
                        break
                except ValueError:             #####################
                    print "Not a valid input." ##### END VALIDATION#
            ## Check if player hit  computer   #####################
            if guess_row == ship1_row and guess_col == ship1_col:
                #Player wins
                #hit = true to break out
                hit = True
                print "It's a hit You win!"
                board[ship1_row - 1][ship1_col - 1] = "X"
                print_board(board)
                #ask user if they want to play again
                response = raw_input("Would you like to play again?")
                while response.lower() not in {'y', 'n', 'yes', 'no'}:  # Fill in the condition (before the colon)
                    response = raw_input("Please enter yes or no: ")
                playagain = response
            elif hit is False and playagain == 'yes' and guess_row != ship1_row and guess_col != ship1_col: #make sure we didnt already win.
                #Player missed. Mark board and computer will go
                print "You missed!"
                board[guess_row - 1][guess_col - 1] = "*"
                print_board(board)
                print ""
                print "Okay my turn"
                print ""
                #make sure computer doesn't pick a spot already picked.
                dup_check = False
                while dup_check == False: 
                    comp_row = int(rand_row(board))
                    comp_col = int(rand_col(board))
                    dup_check = duplicate_validate(comp_row, comp_col)
                if comp_row == player_row and comp_col == player_col:
                    #computer wins
                    hit = True
                    print "Gotcha! Too easy!"
                    board[comp_row - 1][comp_col - 1] = "X"
                    print_board(board)
                    response = raw_input("Would you like to play again?")
                    while response.lower() not in {'y', 'n', 'yes', 'no'}:  # Fill in the condition (before the colon)
                        response = raw_input("Please enter yes or no: ")
                    playagain = response
                else:
                    print ""
                    print ""
                    print "Looks like i missed... your turn!"
                    print ""
                    print ""











else: #play against self
    print "Loner aye? Alright will I place a ship randomly on the board."
    print "Ya got 4 tries to hit it. Good luck!"
    play_again = 'yes'
    while play_again == 'yes':
        #initializes board and coordinates
        board = create_board()
        ship1_row = int(rand_row(board))
        ship1_col = int(rand_col(board))
        print_board(board)
        for turn in range(4): # for loop is the amount of turns they have. In this case 4
            print ""
            #show space ---debug
            #print "ship row " + str(ship1_row)
            #print "ship row " + str(ship1_col)
            print "You have " + str((range(4)[3] + 1) - turn) + " turns left."
            print "~~~~~~~~~~~~~~"
            while True: #This while loop askes for user input. Validates it's an integer between 1 and 5
                try:    #and makes sure it's a coordinate they already guessed
                    guess_row = -3
                    while guess_row < 1 or guess_row > 5:
                        try:
                            guess_row = int(raw_input("Guess Row:")) #get input
                            if guess_validate(guess_row) is False: #check to make sure it's in range
                                print "Invalid input"
                            else:
                                break
                        except ValueError:
                            print "Input not valid"
                    guess_col = -3
                    while guess_col < 1 or guess_col > 5:
                        try:
                            guess_col = int(raw_input("Guess Col:"))
                            #guess_col = 3
                            if guess_validate(guess_col) is False:
                                print "Invalid input"
                            else:
                                break
                        except ValueError:
                            print "Input not valid"
                    if duplicate_validate(guess_row, guess_col) is False: #check to make sure it's not already guessed
                        print "You've already guessed this coordinate!"
                    else:
                        break
                except ValueError:
                    print "Not a valid input."
            print "~~~~~~~~~~~~~~"

            if guess_row == ship1_row and guess_col == ship1_col:
                print "It's a hit You win!"
                board[ship1_row - 1][ship1_col - 1] = "X"
                print_board(board)
                #ask user if they want to play again
                response = raw_input("Would you like to play again?")
                while response.lower() not in {'y', 'n', 'yes', 'no'}:  # Fill in the condition (before the colon)
                    response = raw_input("Please enter yes or no: ")
                playagain = response
                break
            else: #continue game
                if turn != 3:
                    print "Miss!"
                    print "~~~~~~~~~~~~~~"
                    board[guess_row - 1][guess_col - 1] = "*"
                    print_board(board)
                    print " this is turn", turn
                    print "~~~~~~~~~~~~~~ end of continue"
                else: #end game
                    print "~~~~~~~~~~~~~~ start of end else"
                    print "Game over"
                    print "My ship was at row %s, column %s!" % (ship1_col, ship1_row)
                    board[ship1_row - 1][ship1_col - 1] = "X"
                    print "~~~~~~~~~~~~~~"
                    print_board(board)
                    response = raw_input("Would you like to play again?")
                    while response.lower() not in {'y', 'n', 'yes', 'no'}:  # Fill in the condition (before the colon)
                        response = raw_input("Please enter yes or no: ")
                    playagain = response
print "Thanks for playing"

from random import randint

# Game begins
def play():
    # Creates board list
    board = []

    # Creates board of "O" * 5
    for x in range(5):
        board.append(["O"] * 5)

    #Prints board layout
    def print_board(board):
        for row in board:
            print " ".join(row)
    
    print "Let's play Battleship!"
    print_board(board)

    # Creates battleship location
    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)

    # Gameplay
    for turn in range(4):
        # Asks user for guess
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Col: "))
        
        # Compares guesses to battleship location
        # If user guesses correctly
        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!"
            again()
            
        # If user guesses outside of board
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean."
            # If user repeats a previous guess
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            # If user misses battleship
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
                # If all turns have been used, game ends
                if turn == 3:
                    print "Game Over"
                    #print "Ship row: " + ship_row
                    #print "Ship Col: " + ship_col
                    again()
                    break
            # Turn Counter
            print "Turn", turn + 1
            print_board(board)

# Asks user if they would like to play again
def again():
    again = raw_input("Would you like to play again? Enter y/n: ")
    if again == "y":
        play()
    elif again == "n":
        print "Goodbye!"
        print 'Enter "play()" to start a new game!'
    else:
        print 'Does not compute. Enter "play()" to start a new game!'

# Beginning of game      
play()

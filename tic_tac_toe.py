# Create a Tic Tac Toe game.
# Here are the requirements:
# 2 players should be able to play the game (user, computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board
from array import *
from random import randint
exit_game = False
def print_board(board):
    print("Printing board.", exit_game)

    if(exit_game == True):
        return
    print("------------")
    for i in range(0, 3):
        print("|", board[i][0], board[i][1], board[i][2], "|")
#        for j in range(0, 2):
#            print(board[i][j], end =" ")
    print("------------")

# goes through board & generates ordered pair that is a potential response
def rules_function(board, choices, usymbol, csymbol): #board parameter for when it is intelligent
    # Step 1: in most cases, generate random ordered pair, but in certain cases, return intelligent response to prevent
    # user win

    if(board[0][1] == csymbol):
        if(board[1][1] == csymbol):
            if(board[2][1] == " "):
                print("Computer should choose (2, 1)")
                board[2][1] = csymbol
                exit_game = True
                return choices[7]
    if(board[0][2] == csymbol):
        if(board[1][1] == csymbol):
            if(board[2][0] == ' '):
                print("Computer should choose (2, 0)")
                board[2][0] = csymbol
                print("Game over.")
                exit_game = True
                return choices[6]
    elif(board[0][0] == usymbol): #top row
        if(board[0][1] == usymbol):
            if(board[0][2] == usymbol):
                print("Game over.")
                exit_game = True
            elif(board[0][2] == csymbol):
                print("Computer should not choose (0, 2)")
                board[2][0] = csymbol
                return choices[6]
            else:
                print("Computer should choose (0, 2)")
                board[0][2] = csymbol
                return choices[2]
        elif(board[1][0] == usymbol): #left column
            if(board[2][0] == usymbol):
                print("Game over.")
                exit_game = True
            else:
                print("Computer should choose (2, 0)")
        elif(board[1][1] == usymbol): #diagonally to the right
            if(board[2][2]):
                print("Game over.")
                exit_game = True
            else:
                print("Computer should choose (1, 2)")
    elif(board[0][1] == usymbol): #middle column
        if(board[1][1] == usymbol):
            if(board[2][1] == usymbol):
                print("Game over.")
                exit_game = True
            else:
                print("Computer should choose (2, 2)")
        else:
            print("to be fixed.")
            if(board[1][1] == " "):
                board[1][1] == csymbol
                return choices[4]
    elif(board[0][2] == usymbol): #diagonally to the left
        if(board[1][1] == usymbol):
            if(board[2][0] == usymbol):
                print("Game over.")
                exit_game = True
            else:
                print("Computer should choose (2, 0)")
        elif(board[1][2] == usymbol): #right column
            if(board[2][2] == usymbol):
                print("Game over.")
                exit_game = True
            else:
                print("Computer should choose (2, 2)")
    elif(board[1][0] == usymbol): #middle row
        if(board[1][1] == usymbol):
            if(board[1][2] == usymbol):
                print("Game over.")
                exit_game = True
            else:
                print("Computer should choose (1, 2)")
    elif(board[2][0] == usymbol): #bottom row
        if(board[2][1] == usymbol):
            if(board[2][2] == usymbol):
                print("Game over.")
                exit_game = True
                ret = {}
                return ret
            else:
                print("Computer should choose (2, 2)")
    print("rules_function")
    rand_int = randint(0, len(choices))
    print(rand_int)

    return choices[rand_int]

def generate_comp_response(board, comp_symbol):
    print("Generating response...")
    # Step 1: call empty_cells & it returns list of lists. size of list will be used to generate random number
    # based on total # of remaining empty spaces
    possible_choices = empty_cells(board)
    print(possible_choices)
    # Step 2: use rules_function to generate 1 random number which is used to index into the list and generate which row and col
    # will be picked by the computer
    x_y_pair = rules_function(board, possible_choices, user_symbol, comp_symbol)
    print(x_y_pair)
    if(x_y_pair == {}):
        exit(0)
    # Step 3: update the chosen empty space with the computer symbol
    board[x_y_pair[0]][x_y_pair[1]] = comp_symbol
# returns list of <row, col> pairs that identify which cells are empty
def empty_cells(board):
    print("empty_cells()")
    list = {}

    #go through rows & columns in board and return list of lists(row, col each representing an empty space)
    # returns list of lists
    for i in range(0, 3):
        for j in range(0, 3):
            if(board[i][j] == ' '):
                list[i*3+j] = [i, j]
    return list

user_win = False
symbols = ['X', 'O']
error = False
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
user_symbol = input("Welcome to TicTacToe. Would you like to play as 'X' or 'O'?(Case-sensitive)")
if(user_symbol == symbols[0]):
    comp_symbol = symbols[1]
elif(user_symbol == symbols[1]):
    comp_symbol = symbols[0]
else:
    print('That is not one of the options given.')
    error = True
if(error == False):
    print("The computer's symbol is ", comp_symbol)
print_board(board)
# exit_game = False
while(exit_game == False):
    print_board(board)
    print("Exit_game: ", exit_game)
    row_num = int(input("Enter row number(0, 1, 2): "))
    if(row_num != 0 and row_num != 1 and row_num != 2): # check range
        print("Error: That is not one of the given choices. ", row_num)
        error = True
        exit_game = True
    col_num = int(input("Enter column number(0, 1, 2): "))
    if (col_num != 0 and col_num != 1 and col_num != 2):
        print("Error: That is not one of the given choices. ", col_num)
        error = True
        exit_game = True
    if(board[row_num][col_num] != " "):
        print("Error: This cell is taken.")
        continue
    board[row_num][col_num] = user_symbol
    print_board(board)
    #call generate_comp_response which will return a random pair from the list of empty spots
    generate_comp_response(board, comp_symbol)
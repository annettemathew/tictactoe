# Create a Tic Tac Toe game.
# Here are the requirements:
# 2 players should be able to play the game (user, computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board
from array import *
from random import randint
from enum import Enum

class Orientation(Enum):
    TOP = 0
    MIDDLE = 1
    BOTTOM = 2
    LEFT = 3
    CENTER = 4
    RIGHT = 5
    DIAG1 = 6
    DIAG2 = 7


class Turn(Enum):
    USER = 0
    COMP = 1


next_turn = Turn.USER
exit_game = False
avail_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
user_win = False # is this necessary
symbols = ['X', 'O']
error = False
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
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
#converts coordinates of cell to unique key for each cell(0-8)
def conv(i, j):
    return i * 3 + j

#accepts key and returns pair of coordinates
def reverse_conv(key):
    pair = []
    pair.add(key / 3)
    pair.add(key % 3)
    return pair

# this will be called for each of the 8 different orientations
def process_tuple(b, orientation, turn, #next_turn
                   avail_indices):
    if(orientation == Orientation.TOP):
        if(b[0][0] == user_symbol and b[0][1] == user_symbol and b[0][2] == " "):
            # block user win
            if(turn == Turn.COMP):
                b[0][2] = comp_symbol
                avail_indices.remove(conv(0, 2))
                turn = Turn.USER
                return
        elif(b[0][0] == comp_symbol and b[0][1] == comp_symbol and b[0][2] == " "):
            # take (0, 2) and win
            if(turn == Turn.COMP):
                b[0][2] = comp_symbol
                avail_indices.remove(conv(0, 2))
                turn = Turn.USER
                print_board(b)
                exit(0)
        elif(b[0][1] == user_symbol and b[0][2] == user_symbol and b[0][0] == " "):
            if (turn == Turn.COMP):
                b[0][0] = comp_symbol
                avail_indices.remove(conv(0, 0))
                turn = Turn.USER
                return
        elif (b[0][1] == comp_symbol and b[0][2] == comp_symbol and b[0][0] == " "):
            # take (0, 0) and win
            if (turn == Turn.COMP):
                b[0][0] = comp_symbol
                avail_indices.remove(conv(0, 0))
                turn = Turn.USER
                print_board(b)
                exit(0)
        elif (b[0][0] == user_symbol and b[0][2] == user_symbol and b[0][1] == " "):
            if (turn == Turn.COMP):
                b[0][1] = comp_symbol
                avail_indices.remove(conv(0, 1))
                turn = Turn.USER
                return
        elif (b[0][0] == comp_symbol and b[0][2] == comp_symbol and b[0][1] == " "):
            # take (0, 1) and win
            if (turn == Turn.COMP):
                b[0][1] = comp_symbol
                avail_indices.remove(conv(0, 1))
                print_board(b)
                turn = Turn.USER
                exit(0)
    elif(orientation == Orientation.MIDDLE):
        if (b[1][0] == user_symbol and b[1][1] == user_symbol and b[1][2] == " "):
            # block user win
            if (turn == Turn.COMP):
                b[1][2] = comp_symbol
                avail_indices.remove(conv(1, 2))
                turn = Turn.USER
                return
        elif (b[1][0] == comp_symbol and b[1][1] == comp_symbol and b[1][2] == " "):
            # take (1, 2) and win
            if (turn == Turn.COMP):
                b[1][2] = comp_symbol
                avail_indices.remove(conv(1, 2))
                print_board(b)
                turn = Turn.USER
                exit(0)
        elif (b[1][1] == user_symbol and b[1][2] == user_symbol and b[1][0] == " "):
            if (turn == Turn.COMP):
                b[1][0] = comp_symbol
                avail_indices.remove(conv(1, 0))
                next_turn = Turn.USER
                return
        elif (b[1][1] == comp_symbol and b[1][2] == comp_symbol and b[1][0] == " "):
            # take (1, 0) and win
            if (turn == Turn.COMP):
                b[1][0] = comp_symbol
                avail_indices.remove(conv(1, 0))
                print_board(b)
                turn = Turn.USER
                exit(0)
        elif (b[1][0] == user_symbol and b[1][2] == user_symbol and b[1][1] == " "):
            if (turn == Turn.COMP):
                b[1][1] = comp_symbol
                avail_indices.remove(conv(1, 1))
                turn = Turn.USER
                print(turn)
                return
        elif (b[1][0] == comp_symbol and b[1][2] == comp_symbol and b[1][1] == " "):
            # take (1, 1) and win
            if (turn == Turn.COMP):
                b[1][1] = comp_symbol
                avail_indices.remove(conv(1, 1))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
    elif(orientation == Orientation.BOTTOM):
        if (b[2][0] == user_symbol and b[2][1] == user_symbol and b[2][2] == " "):
            # block user win
            if (turn == Turn.COMP):
                b[2][2] = comp_symbol
                avail_indices.remove(conv(2, 2))
                turn = Turn.USER
                print(turn)
                return
        elif (b[2][0] == comp_symbol and b[2][1] == comp_symbol and b[2][2] == " "):
            # take (2, 2) and win
            if (turn == Turn.COMP):
                b[2][2] = comp_symbol
                avail_indices.remove(conv(2, 2))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
        elif (b[2][1] == user_symbol and b[2][2] == user_symbol and b[2][0] == " "):
            if (turn == Turn.COMP):
                b[2][0] = comp_symbol
                avail_indices.remove(conv(2, 0))
                turn = Turn.USER
                print(turn)
                return
        elif (b[2][1] == comp_symbol and b[2][2] == comp_symbol and b[2][0] == " "):
            # take (2, 0) and win
            if (turn == Turn.COMP):
                b[2][0] = comp_symbol
                avail_indices.remove(conv(2, 0))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
        elif (b[2][0] == user_symbol and b[2][2] == user_symbol and b[2][1] == " "):
            if (turn == Turn.COMP):
                b[2][1] = comp_symbol
                avail_indices.remove(conv(2, 1))
                turn = Turn.USER
                print(turn)
                return
        elif (b[2][0] == comp_symbol and b[2][2] == comp_symbol and b[2][1] == " "):
            # take (2, 1) and win
            if (turn == Turn.COMP):
                b[2][1] = comp_symbol
                avail_indices.remove(conv(2, 1))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
    elif(orientation == Orientation.LEFT):
        if (b[0][0] == user_symbol and b[1][0] == user_symbol and b[2][0] == " "):
            # block user win
            if (turn == Turn.COMP):
                b[2][0] = comp_symbol
                avail_indices.remove(conv(2, 0))
                turn = Turn.USER
                print(turn)
                return
        elif (b[0][0] == comp_symbol and b[1][0] == comp_symbol and b[2][0] == " "):
            # take (2, 0) and win
            if (turn == Turn.COMP):
                b[2][0] = comp_symbol
                avail_indices.remove(conv(2, 0))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
        elif (b[0][0] == user_symbol and b[2][0] == user_symbol and b[1][0] == " "):
            if (turn == Turn.COMP):
                b[1][0] = comp_symbol
                avail_indices.remove(conv(1, 0))
                turn = Turn.USER
                print(turn)
                return
        elif (b[0][0] == comp_symbol and b[2][0] == comp_symbol and b[1][0] == " "):
            # take (1, 0) and win
            if (turn == Turn.COMP):
                b[1][0] = comp_symbol
                avail_indices.remove(conv(1, 0))
                turn = Turn.USER
                print(turn)
                print_board(b)
                exit(0)
        elif (b[1][0] == user_symbol and b[2][0] == user_symbol and b[0][0] == " "):
            if (turn == Turn.COMP):
                b[0][0] = comp_symbol
                avail_indices.remove(conv(0, 0))
                turn = Turn.USER
                print(turn)
                return
        elif (b[1][0] == comp_symbol and b[2][0] == comp_symbol and b[0][0] == " "):
            # take (0, 0) and win
            if (turn == Turn.COMP):
                b[0][0] = comp_symbol
                avail_indices.remove(conv(0, 0))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
    elif(orientation == Orientation.CENTER):
        # print("in center")
        if (b[0][1] == user_symbol and b[1][1] == user_symbol and b[2][1] == " "):
            # block user win
            # print("handling (0, 1) + (1, 1) with (2, 1) empty")
            if (turn == Turn.COMP):
                b[2][1] = comp_symbol
                avail_indices.remove(conv(2, 1))
                turn = Turn.USER
                print(turn)
                return
        elif (b[0][1] == comp_symbol and b[1][1] == comp_symbol and b[2][1] == " "):
            # print("Comp symbol center")
            # take (2, 1) and win
            if (turn == Turn.COMP):
                b[2][1] = comp_symbol
                avail_indices.remove(conv(2, 1))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
        elif (b[0][1] == user_symbol and b[2][1] == user_symbol and b[1][1] == " "):
            if (turn == Turn.COMP):
                b[1][1] = comp_symbol
                avail_indices.remove(conv(1, 1))
                turn = Turn.USER
                print(turn)
                return
        elif (b[0][1] == comp_symbol and b[2][1] == comp_symbol and b[1][1] == " "):
            # take (1, 1) and win
            if (turn == Turn.COMP):
                b[1][1] = comp_symbol
                avail_indices.remove(conv(1, 1))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
        elif (b[1][1] == user_symbol and b[2][1] == user_symbol and b[0][1] == " "):
            if (turn == Turn.COMP):
                b[0][1] = comp_symbol
                avail_indices.remove(conv(0, 1))
                turn = Turn.USER
                print(turn)
                return
        elif (b[1][1] == comp_symbol and b[2][1] == comp_symbol and b[0][1] == " "):
            # take (0, 1) and win
            if (turn == Turn.COMP):
                b[0][1] = comp_symbol
                avail_indices.remove(conv(0, 1))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
    elif(orientation == Orientation.RIGHT):
        if (b[0][2] == user_symbol and b[1][2]== user_symbol and b[2][2] == " "):
            # block user win
            if (turn == Turn.COMP):
                b[2][2] = comp_symbol
                avail_indices.remove(conv(2, 2))
                turn = Turn.USER
                return
        elif (b[0][2] == comp_symbol and b[1][2] == comp_symbol and b[2][2] == " "):
            # take (2, 2) and win
            if (turn == Turn.COMP):
                b[2][2] = comp_symbol
                avail_indices.remove(conv(2, 2))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
        elif (b[0][2] == user_symbol and b[2][2] == user_symbol and b[1][2] == " "):
            if (turn == Turn.COMP):
                b[1][2] = comp_symbol
                avail_indices.remove(conv(1, 2))
                turn = Turn.USER
                print(turn)
                return
        elif (b[0][2] == comp_symbol and b[2][2] == comp_symbol and b[1][2] == " "):
            # take (1, 2) and win
            if (turn == Turn.COMP):
                # print("RIGHT: taking (1, 2)")
                b[1][2] = comp_symbol
                avail_indices.remove(conv(1, 2))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
        elif (b[1][2] == user_symbol and b[2][2] == user_symbol and b[0][2] == " "):
            # block user win
            if (turn == Turn.COMP):
                b[0][2] = comp_symbol
                avail_indices.remove(conv(0, 2))
                turn = Turn.USER
                print(turn)
                return
        elif (b[1][2] == comp_symbol and b[2][2] == comp_symbol and b[0][2] == " "):
            # take (0, 2) and win
            if (turn == Turn.COMP):
                b[0][2] = comp_symbol
                avail_indices.remove(conv(0, 2))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
    elif(orientation == Orientation.DIAG1):
        # print("Diag1")
        if (b[0][0] == user_symbol and b[1][1]== user_symbol and b[2][2] == " "):
            # block user win
       #     print("User in diag1")
            if (turn == Turn.COMP):
                b[2][2] = comp_symbol
                avail_indices.remove(conv(2, 2))
                turn = Turn.USER
                print(turn)
                return
        elif (b[0][0] == comp_symbol and b[1][1] == comp_symbol and b[2][2] == " "):
            # take (2, 2) and win
            # print("comp_symbol diag1")
            if (turn == Turn.COMP):
                b[2][2] = comp_symbol
                avail_indices.remove(conv(2, 2))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
        elif (b[0][0] == user_symbol and b[2][2] == user_symbol and b[1][1] == " "):
            if (turn == Turn.COMP):
                b[1][1] = comp_symbol
                avail_indices.remove(conv(1, 1))
                turn = Turn.USER
                print(turn)
                return
        elif (b[0][0] == comp_symbol and b[2][2] == comp_symbol and b[1][1] == " "):
            # take (1, 1) and win
            if (turn == Turn.COMP):
                b[1][1] = comp_symbol
                avail_indices.remove(conv(1, 1))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
        elif (b[1][1] == user_symbol and b[2][2] == user_symbol and b[0][0] == " "):
            if (turn == Turn.COMP):
                b[0][0] = comp_symbol
                avail_indices.remove(conv(0, 0))
                turn = Turn.USER
                print(turn)
                return
        elif (b[1][1] == comp_symbol and b[2][2] == comp_symbol and b[0][0] == " "):
            # take (0, 0) and win
            if (turn == Turn.COMP):
                b[0][0] = comp_symbol
                avail_indices.remove(conv(0, 0))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
    elif(orientation == Orientation.DIAG2):
        if (b[0][2] == user_symbol and b[1][1]== user_symbol and b[2][0] == " "):
            # block user win
            if (turn == Turn.COMP):
                b[2][0] = comp_symbol
                avail_indices.remove(conv(2, 0))
                turn = Turn.USER
                print(turn)
                return
        elif (b[0][2] == comp_symbol and b[1][1] == comp_symbol and b[2][0] == " "):
            # take (2, 0) and win
            if (turn == Turn.COMP):
                b[2][0] = comp_symbol
                avail_indices.remove(conv(2, 0))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
        elif (b[0][2] == user_symbol and b[2][0] == user_symbol and b[1][1] == " "):
            if (turn == Turn.COMP):
                b[1][1] = comp_symbol
                avail_indices.remove(conv(1, 1))
                turn = Turn.USER
                print(turn)
                return
        elif (b[0][2] == comp_symbol and b[2][0] == comp_symbol and b[1][1] == " "):
            # take (1, 1) and win
            if (turn == Turn.COMP):
                b[1][1] = comp_symbol
                avail_indices.remove(conv(1, 1))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
        elif (b[1][1] == user_symbol and b[2][0] == user_symbol and b[0][2] == " "):
            if (turn == Turn.COMP):
                b[0][2] = comp_symbol
                avail_indices.remove(conv(0, 2))
                turn = Turn.USER
                print(turn)
                return
        elif (b[1][1] == comp_symbol and b[2][0] == comp_symbol and b[0][2] == " "):
            # take (0, 2) and win
            if (turn == Turn.COMP):
                b[0][2] = comp_symbol
                avail_indices.remove(conv(0, 2))
                print_board(b)
                turn = Turn.USER
                print(turn)
                exit(0)
    else:
        print("Error: incorrect orientation")
        exit(-1)
# takes in board and symbol(user or computer); detects whether that symbol won
# if so, print board and exit(0)
def detect_win(board, symbol):
    msg = " "
    if(symbol == user_symbol):
        msg = "User "
    else:
        msg = "Computer "
    msg += "won. "
    if(board[0][0] == symbol and board[0][1] == symbol and board[0][2] == symbol):
        print_board(board)
        print(msg)
        exit(0)
    elif(board[1][0] == symbol and board[1][1] == symbol and board[1][2] == symbol):
        print_board(board)
        print(msg)
        exit(0)
    elif (board[2][0] == symbol and board[2][1] == symbol and board[2][2] == symbol):
        print_board(board)
        print(msg)
        exit(0)
    elif (board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol):
        print_board(board)
        print(msg)
        exit(0)
    elif (board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol):
        print_board(board)
        print(msg)
        exit(0)
    elif (board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol):
        print_board(board)
        print(msg)
        exit(0)
    elif (board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol):
        print_board(board)
        print(msg)
        exit(0)
    elif (board[2][0] == symbol and board[1][1] == symbol and board[0][2] == symbol):
        print_board(board)
        print(msg)
        exit(0)

    # goes through board & generates ordered pair that is a potential response
def rules_function(board, turn, #choices,
                     usymbol, csymbol):  # board parameter for when it is intelligent
    # Step 0: Check for user win
    detect_win(board, user_symbol)

    # Step 1: Check for computer win
    detect_win(board, comp_symbol)

    print(avail_indices)
    print(turn)

    # Step 2a: process top row
    process_tuple(board, Orientation.TOP, turn, avail_indices)
    process_tuple(board, Orientation.MIDDLE, turn, avail_indices)
    process_tuple(board, Orientation.BOTTOM, turn, avail_indices)
    process_tuple(board, Orientation.LEFT, turn, avail_indices)
    process_tuple(board, Orientation.CENTER, turn, avail_indices)
    process_tuple(board, Orientation.RIGHT, turn, avail_indices)
    # print("right done. calling diag1")
    process_tuple(board, Orientation.DIAG1, turn, avail_indices)
    # print("diag1 done. ")
    process_tuple(board, Orientation.DIAG2, turn, avail_indices)
    if(turn == Turn.COMP):
        rand_int = randint(0, len(avail_indices) - 1)
        r = (int)(avail_indices[rand_int] / 3)
        c = avail_indices[rand_int] % 3
        print("Indexing into: ", rand_int,  ", avail_index: ", avail_indices[rand_int], ", row: ", r, ", col: " , c)
        board[r][c] = comp_symbol
        avail_indices.remove(rand_int)
        turn = Turn.USER

    # Step 2: in most cases, generate random ordered pair, but in certain cases, return intelligent response to prevent
    # user win

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
        exit(-1) # error exit
    col_num = int(input("Enter column number(0, 1, 2): "))
    if (col_num != 0 and col_num != 1 and col_num != 2): # check range
        print("Error: That is not one of the given choices. ", col_num)
        error = True
        exit_game = True
        exit(-1) # error exit
    avail_indices.remove(row_num * 3 + col_num)
    if(board[row_num][col_num] != " "):
        print("Error: This cell is taken.")
        continue
    board[row_num][col_num] = user_symbol
    next_turn = Turn.COMP
    print_board(board)
    #call generate_comp_response which will return a random pair from the list of empty spots
    # generate_comp_response(board, comp_symbol)
    rules_function(board, next_turn, user_symbol, comp_symbol)
print("Outside while loop")

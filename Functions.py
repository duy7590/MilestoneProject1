Milestone project 1:

#printing the board
from IPython.display import clear_output

def game_interface(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

#Taking user input

def choose_marker():

    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, please pick X or O:").upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#Assigning marker

def place_marker(board,marker,position):
	board[position] = marker

#checking if position is free

def free_space_check(board, position):
	return board[position] == ' '

#checking if board is full

def full_board(board):
	for i in range(1,10):
		if free_space_check(board, i):
			return False
	return True

def winner(board,mark):
	return ((board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[7]==mark and board[4]==mark and board[1]==mark) or
    (board[8]==mark and board[5]==mark and board[2]==mark) or
    (board[9]==mark and board[6]==mark and board[3]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark) or
    (board[1]==mark and board[5]==mark and board[9]==mark))
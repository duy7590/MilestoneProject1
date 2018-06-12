#Milestone project 1:

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

#who goes first

import random

def who_starts():
	if random.randint(0,1) == 0:
		return 'Player 1'
	else:
		return 'Player 2'


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

#checking if won

def winner(board,mark):
	return ((board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[7]==mark and board[4]==mark and board[1]==mark) or
    (board[8]==mark and board[5]==mark and board[2]==mark) or
    (board[9]==mark and board[6]==mark and board[3]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark) or
    (board[1]==mark and board[5]==mark and board[9]==mark))

#assigning marker to position 

def next_move(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not free_space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

#play again?

def play_again():
    return input('Do you want to play again? Write Yes or No').lower().startswith('y')

#the game

print('Welcome to Tic Tac Toe')

while True:
    playingBoard = [' '] * 10
    player1, player2 = choose_marker()
    turn = who_starts()
    print (turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            game_interface(playingBoard)
            position = next_move(playingBoard)
            place_marker(playingBoard,player1,position)

            if winner(playingBoard,player1):
                game_interface(playingBoard)
                print ('Player 1 has won the game')
                game_on = False

            else:
                if full_board(playingBoard):
                    game_interface(playingBoard)
                    print ('The game is a draw')
                    break
                else:
                    turn = 'Player 2'


        else:

            game_interface(playingBoard)
            position = next_move(playingBoard)
            place_marker(playingBoard,player2,position)

            if winner(playingBoard,player2):
                game_interface(playingBoard)
                print ('Player 2 has won the game')
                game_on = False
            
            else:
                if full_board(playingBoard):
                    game_interface(playingBoard)
                    print('the game is a draw')
                    break
                else:
                    turn = 'Player 1'
    
    if not play_again():
        break
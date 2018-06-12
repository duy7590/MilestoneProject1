

# Set the game up here:________________________________________________________________________________

## print out a board.

def display_board(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


## take in a player input and assign their marker as 'X' or 'O'

def player_input():

    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X','O')

    else:
        return ('O','X')


## takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board

def place_marker(board, marker, position):
    board[position] = marker


## Check

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
     (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
     (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
     (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
     (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
     (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
     (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
     (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


## randomly decide which player goes first

import random

def choose_first():
   if random.randint(1,2) == 1:
        print('Player 1 go first')
   else:
        print('Player 2 go first')

## returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):
    return board[position] in  ['1','2','3','4','5','6','7','8','9']

## checks if the board is full and returns a boolean value. True if full, False otherwise

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


##  asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9]:
        position = int(input('Choose your next position: (1-9) '))

    return position

def replay():
    A=input('Do you want to play again? Enter Yes or No: ')
    return A.lower().startswith('y')

def clear_screen():
    print ('\n' * 50)

# while game_on:________________________________________________________________________________

print('Welcome to Tic Tac Toe!')


while True  :
    
    board = ['#','1', '2', '3', '4','5', '6', '7', '8', '9']
    (player1,player2) = player_input()
    turn = choose_first()
    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on == True:
        if turn == 'Player 1 go first':

            display_board(board)
            position = player_choice(board)
            place_marker(board, player1, position)

            if win_check(board, player1):
                display_board(board)
                print('Congratulations! You have won the game!')
                clear_screen()
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    clear_screen()
                    break
                else:
                    turn = 'Player 2 go first'

        else:
            
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2, position)

            if win_check(board, player2):
                display_board(board)
                print('Player 2 has won!')
                clear_screen()
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    clear_screen()
                    break
                else:
                    turn = 'Player 1 go first'

    if not replay():
            break
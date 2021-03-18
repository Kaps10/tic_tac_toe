import random
from IPython.display import clear_output

# 1. Function to display the game board

def display_board(board):
    # Xclear_output()
    # print('\n'*100)
    
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


# 2. Function to take in a player input and assign their marker as 'X' or 'O'

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O ?  ').upper()
        
    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')


# 3. Function that takes in the board list object, a marker ('X' or 'O')
# And a desired position (number 1-9) and assigns it to the board

def place_marker(board, marker, position):
    board[position] = marker


# 4. Function that takes in a board and checks to see if someone has won

def check_win(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# 5. Function that uses the random module to randomly decide which player goes first

def choose_first():
    
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    

# 6. Function that returns a boolean indicating whether a space on the board is freely available

def check_board_space(board, position):
    return board[position] == ' '


# 7. Function that checks if the board is full and returns a boolean value

def full_board_check(board):
    for i in range(1,10):
        if check_board_space(board, i):
            return False
    # Board is full if we return TRUE
    return True


# 8. Function that asks for a player's next position (from no 1-9)
# Then uses the function from step 6 to check if its a free position. If it is, then return the position for later use

def player_choice(board):
    pl_position = 0
    
    while pl_position not in [1,2,3,4,5,6,7,8,9] or not check_board_space(board, pl_position):
        pl_position = int(input('Choose your next position: (1-9)  '))
    
    return pl_position


# 9. Function that asks the player if they want to play again and returns a boolean True if they do want to play again

def replay():
    return input('Do you want to play again? Enter Yes or No:  ').lower().startswith('y')


# 10. IMPORTANT  --   Function to run the game!

print('*****     Welcome to the Tic-Tac-Toe Game - Built in Python     *****')

while True:
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    
    player_turn = choose_first()
    print(player_turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No  ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    # Gameplay - when game_on is TRUE
    while game_on:
        # Player 1's turn
        if player_turn == 'Player 1':
            display_board(the_board)
            
            position = player_choice(the_board)
            
            place_marker(the_board, player1_marker, position)
            
            if check_win(the_board, player1_marker):
                display_board(the_board)
                print('CONGRATULATIONS - PLAYER 1 HAS WON THIS GAME  !!  ')
                game_on = False
            
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ohhh....THE GAME IS TIE !!  ')
                    game_on = False     #break
                else:
                    player_turn = 'Player 2'
        
        # Player 2's turn
        else:
            display_board(the_board)
            
            position = player_choice(the_board)
            
            place_marker(the_board, player2_marker, position)
            
            if check_win(the_board, player2_marker):
                display_board(the_board)
                print('CONGRATULATIONS - PLAYER 2 HAS WON THIS GAME  !!  ')
                game_on = False
            
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ohhh....THE GAME IS TIE !!  ')
                    game_on = False     #break
                else:
                    player_turn = 'Player 1'
    
    if not replay():
        break
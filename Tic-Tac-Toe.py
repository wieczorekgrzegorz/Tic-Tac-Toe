#!/usr/bin/env python
# coding: utf-8

# In[4]:


# v1.0
# A Tic-Tac-Toe game with extra error handling.


# In[5]:


# create empty board slots 
def reset_board():
    board = []
    for i in range(9):
        board.append('-')
    return board


# In[6]:


# This function visualises the Tic-Tac-Toe board
def display_board(board):
    print('\n')
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + '     1 | 2 | 3')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5] + '     4 | 5 | 6')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] + '     7 | 8 | 9')
    print('\n')


# In[7]:


# This function takes care of changing current player
def flip_player(current_player):
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    return current_player


# In[8]:


# This function checks game status each round against victory conditions
def check_victory(board):
    victory_status = [False, False, False, False, False, False, False, False]
    victory_status[0] = board[0] == board[1] == board[2] != '-' # 3 in top row
    victory_status[1] = board[3] == board[4] == board[5] != '-' # 3 in middle row
    victory_status[2] = board[6] == board[7] == board[8] != '-' # 3 in bottom row
    victory_status[3] = board[0] == board[3] == board[6] != '-' # 3 in left column
    victory_status[4] = board[1] == board[4] == board[7] != '-' # 3 in middle column
    victory_status[5] = board[2] == board[5] == board[8] != '-' # 3 in right column
    victory_status[6] = board[0] == board[4] == board[8] != '-' # 3 diagonal \
    victory_status[7] = board[2] == board[4] == board[6] != '-' # 3 diagonal /
    for test in victory_status:
        if test == True:
            return True
    return False


# In[9]:


# this functions provides the Player to replay the game after last one was finished
def play_again():
    legal_answers = ['y', 'yes', 'sure', 'ok']
    print()
    #ask Player whether to play again
    players_input = input('Play again? (y / any key): ')
    print()
    print()
    if players_input.lower() in legal_answers:
        play_game()
    else:
        print('I hope you enjoyed the game! See you soon!')
        return False


# In[10]:


# This function checks whether conditions for game finish were met already
# and returns the result if they were
def check_if_game_is_on(current_player,board):
    # check whether last Player's move was victorious
    if check_victory(board):
#     if check_rows(board) or check_columns(board) or check_diagonals(board):
        winner = flip_player(current_player)
        print('Congratulations, ' + winner +  '! You won!')
        return play_again()
    # check whether game ended in a tie
    elif '-' not in board:
        print('It\'s a tie!')
        return play_again()
    # if no winner yet and still empty slots on the board: game on!
    else:
        return True


# In[11]:


# This function takes care of turns handling by: 
# 1. Informing which player's turn it is,
# 2. Validation of player's input vs legal board slot number (1 - 9)
# 3. Validation of player's input vs free board slots
def handle_turn(current_player, board, turn):
    print('Turn #' + str(turn))
    print('   ' + current_player + ', it\'s your move.')
    
    # define legal input from players (digits 1-9)
    legal_positions = []
    for i in range(9):
        legal_positions.append(i + 1)
    
    # This loop handles possible errors
    while True:
        #ask Player to chose position to take
        players_input = input('   Choose board position (1 - 9): ')
        #check whether Player's input is a number
        try:
            position = int(players_input)
        #if not print error message and return to the begining of the while loop
        except ValueError:
            print('   Error: illegal input. You can only choose digits between 1 and 9.')
            continue
        else:
            # check whether Player's input was a digit between 1 and 9
            if position not in legal_positions:
                print('   Error: illegal input. You can only choose digits between 1 and 9.')
                continue
            # check whether Player's input chose an empty slot
            if board[int(position) - 1] != '-':
                print('   Position ' + str(position) + ' is already taken. Choose another position.')
                continue
            break
    
    position = position - 1 # -1 because board is a list
        
    board[position] = current_player
    display_board(board)


# In[12]:


def play_game():  
    board = reset_board()
    current_player = 'X'
    turn = 0
    
    print('Welcome to a Tic-Tac-Toe game.')
    
    display_board(board)
    
    while check_if_game_is_on(current_player,board):
        handle_turn(current_player, board, turn)
        current_player = flip_player(current_player)
        turn += 1


# In[13]:


play_game()


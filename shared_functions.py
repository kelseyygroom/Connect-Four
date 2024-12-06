import connectfour

def print_board(game_board, columns, rows):
    '''
    Given a game board state as a two-dimensional list, prints the game board
    with column markers.
    '''

    for num in range(1, columns + 1):
        if num < 9:
            print(num, end='  ')
        elif num >= 9:
            print(num, end=' ')
    print()
    
    
    
    for column in range(rows):
        for i, v in enumerate(game_board):
            if v[column] == 0:
                print('.', end='  ')
            elif v[column] == 1:
                print('R', end='  ')
            elif v[column] == 2:
                print('Y', end='  ')
        print()


def won(game_state):
    '''
    Checks if the game was won, using connectfour functions and prints who
    the winner is. Returns True or False based on if game is won.
    '''


    won = connectfour.winner(game_state)
    if won == 0:
        return False
    elif won == 1:
        print('\nWINNER: RED')
        return True
    elif won == 2:
        print('\nWINNER: YELLOW')
        return True


def size_valid():
    '''Ensures that the dimensions of the board entered are valid.'''

    while True:
        size = input('Please enter the dimensions of the board, separated by a space (the maximum board size is 20x20):\n')
        components = size.split()
        if len(components) != 2:
            print('ERROR: You must input the column and row size.\n')
            continue
        if len(components) == 2:
            columns = components[0]
            rows = components[1]

        try:
            int(columns)
            int(rows)
        except:
            print('ERROR: your input must contain two integers.\n')
            continue
            
        break

    columns = int(columns)
    rows = int(rows)

    return columns, rows
    



def valid_move(move, columns):
    '''
    Ensures that a move entered is valid. Returns T/F for valid in addition
    to the user move.
    '''

    valid_inputs = ['DROP', 'POP']
        
    if not(move.isspace()):
        move_lst = move.split()
    else:
        print('INVALID')
        return False, None

    if len(move_lst) != 2:
        print('INVALID')
        return False, None
    else:
        user_move = move_lst[0]
        try:
            col = int(move_lst[1]) - 1
        except:
            print('INVALID')
            return False, None
        else:
            if (col) not in range(columns):
                print('INVALID')
                return False, None
            
    if user_move not in valid_inputs:
        print('INVALID')
        return False, None

    return True, user_move, col



def move(user_move, state, col):
    '''Executes a move the user or server requested.'''
    
    if user_move == 'DROP':
        try:
            state = connectfour.drop(state, col)
        except:
            print('INVALID')
            return False
    elif user_move == 'POP':
        try: 
            state = connectfour.pop(state, col)
        except:
            print('INVALID')
            return False

    return state

    

def get_turn(turn):
    '''Returns whose turn it is.'''
    
    if turn == 1:
        return 'RED'
    elif turn == 2:
        return 'YELLOW'
    

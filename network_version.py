import connectfour
import shared_functions
import network_functions


def host_port():
    host = input('Please specify a host:\n')

    invalid = True
    
    while invalid:
        port = input('Please specify a port:\n')

        try:
            port = int(port)
        except:
            print('Port number must be an integer.')
            continue
        else:
            return host, port


def get_username():
    invalid = True
    
    while invalid:
        username = input('Please specify a username:\n')

        if not(username.isalpha()):
            print('ERROR: Please enter a valid username.')
            continue
        else:
            return username


if __name__ == '__main__':

    # get input of host name and port number
    server = host_port()
    
    host = server[0]
    port = server[1]
    
    
    # attempt to connect
    try:
        c = network_functions.connect(host, port)
    except:
        print('ERROR: Unable to connect. Program ended.')
        quit()


    # ask for username
    username = get_username()


    # execute initial "hello" protocol
    network_functions.intro_protocol(c, username)


    # ask for cimensions
    size = shared_functions.size_valid()

    columns = size[0]
    rows = size[1]


    # create initial game state
    state = connectfour.new_game(columns, rows)
    board = state.board
    turn = state.turn
    
    shared_functions.print_board(board, columns, rows)


    # send AI message
    ai = f'AI_GAME {columns} {rows}'

    network_functions.write(c, ai)
    network_functions.ready(c)


    # start game loop
    game_in_progress = True

    while game_in_progress:

        # red move first!
        move = input()

        valid = shared_functions.valid_move(move, columns)
        if not(valid[0]):
            continue
        else:
            r_move = valid[1]
            col = valid[2]


        r_state = shared_functions.move(r_move, state, col)
        if r_state == False:
            continue
        else:
            state = r_state
            board = state.board
            turn = state.turn

        # send move to server
        network_functions.write(c, move)

        # recieve 'okay'
        y_turn = network_functions.okay(c)

        # check game over and print board
        game_over = shared_functions.won(state)
        shared_functions.print_board(board, columns, rows)

        if game_over:
            break
        
        print(y_turn)
        
        # recieve server move and ensure it's in the expected format
        s_full = network_functions.valid_server_move(c, columns)
        
        if s_full == False:
            quit()
        
        s_move = s_full[0]
        
        s_col = s_full[1]
        print(s_move + ' ' + str(s_col + 1))
        
        
        # execute server move
        s_state = shared_functions.move(s_move, state, s_col)
        state = s_state
        board = state.board
        turn = state.turn
        
        
        # print board
        shared_functions.print_board(board, columns, rows)
        
        # receive 'ready'
        network_functions.ready(c)

        
        # check that game is over and continue if game in progress
        game_over = shared_functions.won(state)
        
        if game_over:
            break
        else:
            continue
        

    
            
        

import connectfour
import shared_functions


if __name__ == '__main__':

    size = shared_functions.size_valid()

    columns = size[0]
    rows = size[1]
    
    # start game; get gamestate and board. print board and turn.
    state = connectfour.new_game(columns, rows)
    board = state.board
    turn = state.turn
    
    shared_functions.print_board(board, columns, rows)

    print(shared_functions.get_turn(turn) + ' TURN:')


    game_in_progress = True
    
    while game_in_progress:

        # get red_player turn
        move = input()

        valid = shared_functions.valid_move(move, columns)
        if not(valid[0]):
            continue
        else:
            user_move = valid[1]
            col = valid[2]
    

        r_move = shared_functions.move(user_move, state, col)
        if r_move == False:
            continue
        else:
            state = r_move
            board = state.board
            turn = state.turn
        
        game_over = shared_functions.won(state)
        
        if game_over:
            shared_functions.print_board(board, columns, rows)
            break
        else:
            shared_functions.print_board(board, columns, rows)
            print(shared_functions.get_turn(turn) + ' TURN:')
            continue                     









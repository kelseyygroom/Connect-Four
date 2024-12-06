from collections import namedtuple
import socket


ConnectFour = namedtuple('ConnectFour',
                         ['socket', 'inp', 'output'])


def connect(host, port):
    '''Connects to a server given the host and port name. Returns nothing.'''
    
    c4_socket = socket.socket()

    c4_socket.connect((host, port))

    c4_input = c4_socket.makefile('r')
    c4_output = c4_socket.makefile('w')

    return ConnectFour(
        socket = c4_socket,
        inp = c4_input,
        output = c4_output)


def close(connection):
    '''
    Given a connection, disconnects from a server and closes all pseudofiles
    and sockets given a connection. Returns nothing.
    '''

    connection.inp.close()
    connection.output.close()
    connection.socket.close()


def write(connection, line):
    '''
    Given a connection and a desired phrase, sends output to a server by
    writing to and flushing the output pseudofile created in connect().
    Returns nothing.
    '''
    
    connection.output.write(line + '\r\n')
    connection.output.flush()


def read(connection):
    '''
    Given a connection, reads output from the server, stripping the newline
    from the end. Returns the line read.
    '''
    
    return connection.inp.readline().rstrip('\n')


def ready(c):
    '''
    Ensures that server is adhering to the protocol, otherwise closes
    connection immediately. Prints the turn.
    '''
    
    line = read(c)
    if line != 'READY':
        close(c)
    else:
        print('RED TURN:')


def okay(c):
    '''
    Ensures that server is adhering to the protocol, otherwise closes
    connection immediately. Prints the turn.
    '''
    
    line = read(c)
    if line != 'OKAY' and line != 'INVALID':
        close(c)
    else:
        return 'YELLOW TURN:'


def valid_server_move(c, columns):
    '''
    Ensures that server is providing valid moves (adhering to protocol),
    otherwise closes connection immediately.
    '''
    
    move = read(c)
    valid_inputs = ['DROP', 'POP']
    
    if not(move.isspace()):
        move_lst = move.split()
    else:
        close(c)
        return False

    if len(move_lst) != 2:
        close(c)
        return False
    else:
        user_move = move_lst[0]
        try:
            col = int(move_lst[1]) - 1
        except:
            close(c)
            return False
        else:
            if (col) not in range(columns):
                close(c)
                return False
            
    if user_move not in valid_inputs:
        close(c)
        return False

    return user_move, col


def intro_protocol(connection, username):
    '''Initiates protocol by sending welcome message'''
    
    first_message = f'I32CFSP_HELLO {username}'
    write(connection, first_message)
    
    welcome = read(connection)
    if (welcome != 'WELCOME ' + username) and (welcome != 'ERROR'):
        close(connection)
    else:
        print(welcome)



# Connect-Four

This project implements a Python-based connect four game that can be played locally on the shell or over a network by connecting to a server. I utilized socket programming and client-server protocols (an ICS32 Connect Four Server Protocol developed for the course).

The Python shell version allows two users to play connect four locally, with the board and moves displayed in the terminal. The networked version allows users to play against an AI via the Connect Four server.

```connectfour.py``` implements game logic.

```shell_version.py``` implements the game loop for the shell version of connect four. It processes the size of the board and both users moves.

```shared_functions.py``` hosts any shared shell version and network version functions. It processes valid board sizes, valid moves, when the game is won, and keeps track of user turns.

```network_version.py``` and ```network_functions.py``` implement the network version of the connect four game. It handles the ICS 32 protocol, connecting to the server, and processing moves made by the client (local user) and the server.

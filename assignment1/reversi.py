#
# Simon Failla
# SID: 30661293
#

import copy

# Converts an integer in the set {0, 1, 2} into its character
# representation on the board.
def convert_board_element(b):
    return ".BW"[b]

# Converts a coordinate of the format [r, c] into its user friendly
# name e.g. e4, a1, h7
def convert_coordinate(pos):
    return "abcdefgh"[pos[1]] + str(pos[0]+1)

# Returns whether or not the row and column is valid for an 8x8 board.
def in_bounds(r, c):
    return r >= 0 and c >= 0 and r < 8 and c < 8

# Returns the number of 'player's opponent.
def get_opponent(player):
    if player == 1:
        return 2
    else:
        return 1

# Converts a string in the format 'a1' into its coordinate, e.g. [0, 0].
def position(string):
    string = string.lower()
    if len(string) != 2:
        return None
    if not string[0].isalpha():
        return None
    if not string[1].isdigit():
        return None
    if string[0] not in "abcdefgh":
        return None
    return (int(string[1])-1, "abcdefgh".index(string[0]))

# Returns a new board represented by a list of lists, with the center
# tiles initialized to the initial player tiles.
def new_board():
    board = [[0]*8, [0]*8, [0]*8, [0]*8,
             [0]*8, [0]*8, [0]*8, [0]*8]
    board[3][3] = 2;
    board[4][4] = 2;
    board[4][3] = 1;
    board[3][4] = 1;
    return board

# Prints the board in a human friendly format.
def print_board(board):
    print("  a b c d e f g h")

    for i, row in enumerate(board):
        # For every row, construct a string to print to the console.
        toprint = str(i + 1) + " "
        for col in row:
            toprint += convert_board_element(col) + " "
        if i == 2:
            toprint += " --- Scores ---"
        if i == 3:
            toprint += " Black (P1): " + str(score(board)[0])
        if i == 4:
            toprint += " White (P2): " + str(score(board)[1])
        print(toprint)

# Returns a list of coordinates of tiles which would be flipped if
# 'player' was to place a tile on 'board' at 'pos'. The result does not
# include the position that the player is placing at (pos).
def get_changes(board, player, pos):
    directions = [
        (-1, -1),
        (-1,  0),
        (-1,  1),
        ( 0, -1),
        ( 0,  1),
        ( 1, -1),
        ( 1,  0),
        ( 1,  1)
    ]
    changes = []
    for d in directions:
        changes += get_enclosed(board, player, pos, d)

    return changes

# Returns the next state of the game after 'player' plays a tile on
# 'board' at 'pos'.
# Assumes that 'pos' is a valid move for the player.
def next_state(board, player, pos):
    next_board = copy.deepcopy(board)
    changes = get_changes(next_board, player, pos)
    for p in changes:
        next_board[p[0]][p[1]] = player

    # get_changes does not account for changing the tile at 'pos', so
    # we will do it ourselves.
    next_board[pos[0]][pos[1]] = player
    return (next_board, get_opponent(player))

# Returns a list of coordinates of tiles that would be changed if
# 'player' plays a tile on 'board' at 'pos', only tests the direction
# given by 'direct'. The result may be empty, in which case, there is no
# possible move for this direction.
def get_enclosed(board, player, pos, direct):
    other = get_opponent(player)

    r = pos[0]
    c = pos[1]

    # Make sure that 'pos' is en empty tile.
    if board[r][c] != 0:
        return []

    # Increase in the direction so that we dont count the tile
    # at 'pos'.
    r += direct[0]
    c += direct[1]

    res = []

    # Early exit if the tile next to us does not belong to the opponent.
    if not in_bounds(r, c) or board[r][c] != other:
        return []

    # Loop until we reach either the edge of the board or we exit early.
    while in_bounds(r, c):
        # Get the tile at current coordinates and increment them.
        t = board[r][c]

        # If we hit an empty tile, then this move does not enclose.
        if t == 0:
            return []

        # If we hit a tile which belongs to the player, return true.
        # We know we have at least one opponent tile between here and
        # 'pos', as we made sure of that prior to the while loop.
        if t == player:
            return res

        res.append([r, c])
        r += direct[0]
        c += direct[1]

    # If we reach the end of the board and we have not found a tile which
    # would exit us, we assume this is an invalid move.
    return []

# If 'player' plays a tile on 'board' at 'pos', returns true if it
# encloses the opponents tiles in a given direction.
def enclosing(board, player, pos, direct):
    return len(get_enclosed(board, player, pos, direct)) != 0

# Returns a list of coordinates which represent all the valid moves that
# 'player' could make on 'board'.
def valid_moves(board, player):
    directions = [
        (-1, -1),
        (-1,  0),
        (-1,  1),
        ( 0, -1),
        ( 0,  1),
        ( 1, -1),
        ( 1,  0),
        ( 1,  1)
    ]
    result = []
    for r in range(8):
        for c in range(8):
            for d in directions:
                if enclosing(board, player, (r, c), d):
                    result.append((r, c))
    return result

# Returns a list of numbers representing the players scores [p1, p1].
def score(board):
    black = 0
    white = 0
    for row in board:
        for col in row:
            if col == 1:
                black += 1
            elif col == 2:
                white += 1

    return (black, white)

# Returns the best possible move a player can make, or 'None' if there
# are no possible moves.
def get_optimal_move(board, player):
    possible_moves = valid_moves(board, player)
    if len(possible_moves) == 0:
        # No possible moves.
        return None

    # Assume the first move is the best move.
    best_move = possible_moves[0]
    best_changes = get_changes(board, player, best_move)

    # Loop all possible moves to see if we can find a better one.
    for move in possible_moves:
        changes = get_changes(board, player, move)
        if len(changes) > len(best_changes):
            best_move = move
            best_changes = changes

    return best_move

# Returns true if 'player' has at least one valid move they could make.
def can_move(board, player):
    return len(valid_moves(board, player)) != 0

# Gets and processes user input for 'player', returns a coordinate if
# the player entered one, or returns None if the player quit the game.
def get_user_move(board, player, is_cpu):
    # If the user is the computer, calculate the most optimal move.
    if is_cpu:
        return get_optimal_move(board, player)

    while True:
        cmd = input("p" + str(player) + "> ")

        # Cheat mode: dont enter any input.
        # if cmd == "":
        #    return get_optimal_move(board, player)

        if cmd == "q":
            return None

        pos = position(cmd)
        if pos == None:
            print("invalid move")
            continue
        elif not pos in valid_moves(board, player):
            print("invalid move")
            continue
        else:
            return pos

def print_game_end(board):
    print("--- Game Over ---")
    scores = score(board)
    print("  Player 1: " + str(scores[0]))
    print("  Player 2: " + str(scores[1]))
    if scores[0] > scores[1]:
        print("Player 1 wins!")
    elif scores[1] > scores[0]:
        print(" Player 2 wins!")
    else:
        print("     Draw!")
    print("")

def run_two_players():
    board = new_board()
    print_board(board)
    current_player = 1

    while can_move(board, current_player):
        pos = get_user_move(board, current_player, False)
        if pos == None:
            break

        next = next_state(board, current_player, pos)
        board = next[0]
        current_player = next[1]
        print_board(board)

    print_game_end(board)
    print("[Enter] Return to menu")
    input("")

def run_one_player():
    board = new_board()
    print_board(board)
    current_player = 1

    while can_move(board, current_player):
        is_cpu = current_player == 2

        pos = get_user_move(board, current_player, is_cpu)
        if pos == None:
            break

        if is_cpu:
            print(" [ cpu plays " + convert_coordinate(pos) + " ]")

        next = next_state(board, current_player, pos)
        board = next[0]
        current_player = next[1]
        print_board(board)

    print_game_end(board)
    print("[Enter] Return to menu")
    input("")

def print_main_menu():
    print("______                        _ ")
    print("| ___ \                      (_)")
    print("| |_/ /_____   _____ _ __ ___ _ ")
    print("|    // _ \ \ / / _ \ '__/ __| |")
    print("| |\ \  __/\ V /  __/ |  \__ \ |")
    print("\_| \_\___| \_/ \___|_|  |___/_|")
    print("")
    print("         [1] One Player      ")
    print("         [2] Two Player      ")
    print("         [3] Quit            ")
    print("")

#### Entry Point ####
#print_main_menu()

#while True:
#    selection = input("> ")
#    if selection == "1":
#        run_one_player()
#        print_main_menu()
#    elif selection == "2":
#        run_two_players()
#        print_main_menu()
#    elif selection == "3":
#        break

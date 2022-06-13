# write your code here
def move_to_tuple(move):
    return int(move[0]), int(move[2])


def move_to_board(move):
    move = move_to_tuple(move)
    if move == (1, 1):
        return 0
    elif move == (1, 2):
        return 1
    elif move == (1, 3):
        return 2
    elif move == (2, 1):
        return 3
    elif move == (2, 2):
        return 4
    elif move == (2, 3):
        return 5
    elif move == (3, 1):
        return 6
    elif move == (3, 2):
        return 7
    elif move == (3, 3):
        return 8


def count_marks(board, mark):
    return len([m for m in board if m == mark])


def validate_count(board):
    return 0 <= abs(count_marks(board, "X") - count_marks(board, "O")) <= 1


def validate_rows(board, mark):
    for i in range(0, 9, 3):
        marks = 0
        if board[i] == mark:
            marks += 1
        if board[i + 1] == mark:
            marks += 1
        if board[i + 2] == mark:
            marks += 1
        if marks == 3:
            return True

    return False


def validate_cols(board, mark):
    for i in range(3):
        marks = 0
        if board[i] == mark:
            marks += 1
        if board[i + 3] == mark:
            marks += 1
        if board[i + 6] == mark:
            marks += 1
        if marks == 3:
            return True

    return False


def validate_diagonals(board, mark):
    return (board[0] == mark and board[4] == mark and board[8] == mark) \
           or (board[2] == mark and board[4] == mark and board[6] == mark)


def check_impossible(board):
    return (check_winner(board, "X") and check_winner(board, "O")) or \
           not validate_count(board)


def check_game_not_finished(board):
    return not (validate_rows(board, "X") or
                validate_cols(board, "X")) and \
           not (validate_rows(board, "O") or
                validate_cols(board, "O")) and \
           count_marks(board, " ") > 0


def check_draw(board):
    return not (validate_rows(board, "X") or
                validate_cols(board, "X") or
                validate_diagonals(board, "X")) and \
           not (validate_rows(board, "O") or
                validate_cols(board, "O") or
                validate_diagonals(board, "O")) and \
           count_marks(board, " ") == 0


def check_winner(board, mark):
    return validate_rows(board, mark) or \
            validate_cols(board, mark) or \
            validate_diagonals(board, mark)


def check_state(board):
    if check_game_not_finished(board):
        return False
    elif check_draw(board):
        print_draw()
    elif check_winner(board, "X") and not check_impossible(board):
        print_winner("X")
    elif check_winner(board, "O") and not check_impossible(board):
        print_winner("O")
    return True


def check_move_input_length(move):
    return len(move) == 3


def check_occupied(board, move):
    return board[move_to_board(move)] == " "


def check_move_input_type(move):
    try:
        _ = int(move[0])
        _ = int(move[2])
    except ValueError:
        return False
    else:
        return True


def check_move_numbers(move):
    row = int(move[0])
    col = int(move[2])
    return 1 <= row <= 3 and 1 <= col <= 3


def check_move_input(board, move):
    if not check_move_input_length(move) or not check_move_input_type(move):
        print_should_be_numbers()
        return False
    elif not check_move_numbers(move):
        print_should_be_1_to_3()
        return False
    elif not check_occupied(board, move):
        print_occupied()
        return False

    return True


def print_game_not_finished():
    print('Game not finished')


def print_draw():
    print('Draw')


def print_winner(winner):
    print(f'{winner} wins')


def print_impossible():
    print('Impossible')


def print_occupied():
    print('This cell is occupied! Choose another one!')


def print_should_be_numbers():
    print('You should enter numbers!')


def print_should_be_1_to_3():
    print('Coordinates should be from 1 to 3')


def print_dashes():
    print("---------")


def print_board(board):
    print_dashes()
    i = 0
    for j in range(3):
        row = "| "
        for k in range(3):
            row = row + board[i] + " "
            i += 1
        row = row + "|"
        print(row)

    print_dashes()


play = "         "
print_board(play)
player = True
while True:
    player_move = input()
    if check_move_input(play, player_move):
        if player:
            if move_to_board(player_move) < 8:
                play = play[:move_to_board(player_move)] + "X" + play[move_to_board(player_move) + 1:]
                print_board(play)
            else:
                play = play[:move_to_board(player_move)] + "X"
                print_board(play)

        else:
            if move_to_board(player_move) < 8:
                play = play[:move_to_board(player_move)] + "O" + play[move_to_board(player_move) + 1:]
                print_board(play)
            else:
                play = play[:move_to_board(player_move)] + "O"
                print_board(play)

        if check_state(play):
            break

        player = not player

# write your code here
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
           count_marks(board, "_") > 0


def check_draw(board):
    return not (validate_rows(board, "X") or
                validate_cols(board, "X") or
                validate_diagonals(board, "X")) and \
           not (validate_rows(board, "O") or
                validate_cols(board, "O") or
                validate_diagonals(board, "O")) and \
           count_marks(board, "_") == 0


def check_winner(board, mark):
    return validate_rows(board, mark) or \
            validate_cols(board, mark) or \
            validate_diagonals(board, mark)


def check_state(board):
    if check_impossible(board):
        print_impossible()
    else:
        if check_game_not_finished(board):
            print_game_not_finished()
        elif check_draw(board):
            print_draw()
        elif check_winner(board, "X") and not check_impossible(board):
            print_winner("X")
        elif check_winner(board, "O") and not check_impossible(board):
            print_winner("O")
    # elif check_impossible(board):


def print_game_not_finished():
    print('Game not finished')


def print_draw():
    print('Draw')


def print_winner(winner):
    print(f'{winner} wins')


def print_impossible():
    print('Impossible')


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


play = input()
print_board(play)
check_state(play)

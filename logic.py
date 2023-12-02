def invalid(row,col,opt):
    if (row,col) in opt :
        return True
    return False

def check_win(board,player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def min_max(c_board, AI=True):
    cp = c_board[:]
    best_result = -1
    best_move = -1
    if AI:
        best_result = -20  # worst case -> -10
        for i in range(3):
            for j in range(3):
                if c_board[i][j] == ' ':
                    cp[i][j] = 'O'
                    if check_win(cp, 'O'):
                        result = 10
                    elif check_draw(cp):
                        result = 0
                    else:
                        result, _ = min_max(cp, False)

                    cp[i][j] = ' '

                    if result > best_result:
                        best_result = result
                        best_move = (i, j)

        return best_result, best_move
    else:
        best_result = 20  # worst case -> 10
        for i in range(3):
            for j in range(3):
                if cp[i][j] == ' ':
                    cp[i][j] = 'X'
                    if check_win(cp, 'X'):
                        result = -10
                    elif check_draw(cp):
                        result = 0
                    else:
                        result, _ = min_max(cp, True)

                    cp[i][j] = ' '

                    if result < best_result:
                        best_result = result
                        best_move = (i, j)
        return best_result, best_move
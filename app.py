def print_board(board):
    print("-------")
    for i in range(3):
        print(f"|{board[i][0]}|{board[i][1]}|{board[i][2]}|")
        print("-------")


def check_win(board, player):
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
                    cp[i][j] = 'X'
                    if check_win(cp, 'X'):
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
                    cp[i][j] = 'O'
                    if check_win(cp, 'O'):
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


def instruction():
    symb_board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    print("Type the Character to Fill the Respective Places")
    print_board(symb_board)


def encode(a):
    choice = int(a)-1
    row, col = choice//3, choice % 3
    return row, col


def decode(row, col):
    choice = row*3 + col + 1
    return choice


def start_game():

    print("\t\tTIC TAC TOE")
    instruction()
    GAME = True
    filled = []
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    while GAME:
        # AI Turns
        print("AI is choosing......")
        score,pos = min_max(board)
        row,col = pos
        print(f"AI choice {row},{col}")
        choice = decode(row, col)
        board[row][col] = "X"
        filled.append(choice)


        #terminal conditions
        print_board(board)
        result = check_win(board,'X')
        if result :
            print("AI Won The Game")
            break
        if check_draw(board):
            print("The Match is Draw")
            break

        #Human turns
        options =[i for i in range(1,11)]
        while True:
            choice = input("Enter the choice where to fill (1 to 9):")
            if choice.isdigit():
                choice = int(choice)
            else:
                choice = -1

            if choice not in options or choice in filled :
                print("Invalid choice")
            else :
                row,col = encode(choice)
                board[row][col] = 'O'
                filled.append(choice)
                break
        #terminal conditions
        print_board(board)
        result = check_win(board,'O')
        if result:
            print("You Won the Game")
            break
        if check_draw(board):
            print("The Match is Draw")
            break
    
    opt = input("Enter 1 to continue otherwise press some other key to exit the game : ")
    if opt.isdigit():
        if int(opt) == 1:
            start_game()


if __name__ == '__main__':
    start_game()
            
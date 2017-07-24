from IPython.display import clear_output

# globals
board = [' '] * 10
game_state = True
announce = ''


def reset_board():
    global board, game_state
    board = [' '] * 10
    game_state = True


def display_board():
    clear_output()
    print('     |     |     ')
    print('  ' + board[7] + '  ' + '|''  ' + board[8] + '  ' + '|''  ' + board[9] + '  ')
    print('-----|-----|-----')
    print('  ' + board[4] + '  ' + '|''  ' + board[5] + '  ' + '|''  ' + board[6] + '  ')
    print('-----|-----|-----')
    print('  ' + board[1] + '  ' + '|''  ' + board[2] + '  ' + '|''  ' + board[3] + '  ')
    print('     |     |     ')


def win_check(board_check, mark):
    if (board_check[7] == board_check[8] == board_check[9] == mark) or \
        (board_check[4] == board_check[5] == board_check[6] == mark) or \
        (board_check[1] == board_check[2] == board_check[3] == mark) or \
        (board_check[1] == board_check[4] == board_check[7] == mark) or \
        (board_check[2] == board_check[5] == board_check[8] == mark) or \
        (board_check[3] == board_check[6] == board_check[9] == mark) or \
        (board_check[9] == board_check[5] == board_check[1] == mark) or \
            (board_check[7] == board_check[5] == board_check[3] == mark):
        return True
    else:
        return False


def full_board_check(ck_board):
    if " " in ck_board[1:]:
            return False
    else:
        return True


def ask_player(num):
    global board
    pos = 'Please enter the position for your mark ' + num
    while True:
        try:
            choice = int(input(pos))
        except ValueError:
            print("Please use any number between 1-9")
            continue

        if board[choice] == " ":
            board[choice] = num
            break
        else:
            print("The space is filled")
            continue


def player_choice(mark):
    global board, game_state, announce
    announce = ''
    mark = str(mark)
    ask_player(mark)

    if win_check(board, mark):
        clear_output()
        display_board()
        announce = mark + "  wins"
        game_state = False

    clear_output()
    display_board()

    if full_board_check(board):
        announce = "Its a TIE"
        game_state = False

    return game_state, announce


def play_game():
    reset_board()
    global announce, game_state

    x = 'x'.upper()
    o = 'O'.upper()

    while True:
        clear_output()
        display_board()

        game_state, announce = player_choice(x)
        print(announce)
        if game_state is not True:
            break

        game_state, announce = player_choice(o)
        print(announce)
        if game_state is not True:
            break

    rm = input("Play again, y/n")
    if rm == 'y':
        play_game()
    else:
        print("Thanks for playing")

play_game()

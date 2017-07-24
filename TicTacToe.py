from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print('     |     |     ')
    print('  ' + board[7] + '  ' + '|''  ' + board[8] + '  ' + '|''  ' + board[9] + '  ')
    print('-----|-----|-----')
    print('  ' + board[4] + '  ' + '|''  ' + board[5] + '  ' + '|''  ' + board[6] + '  ')
    print('-----|-----|-----')
    print('  ' + board[1] + '  ' + '|''  ' + board[2] + '  ' + '|''  ' + board[3] + '  ')
    print('     |     |     ')


def player_input():
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = input("Please enter 'X' or 'O'").upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[9] == mark and board[5] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[1] == mark))


def choose_first():
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'


def space_check(board, position):
    return board[position]


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = ''
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose your next position')
    return int(position)


def replay():
    return input("Play again??").lower().startswith('y')

print("Play Tic Tac Toe")
while True:
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first')

    game_on = True

    while game_on:
        if turn == 'player1':
            display_board(the_board)
            pos = player_choice(the_board)
            place_marker(the_board, player1_marker, pos)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Congratulations Player 1,You won the Game")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Its a Draw")
                    break
                else:
                    turn = 'player2'
        else:
            display_board(the_board)
            pos = player_choice(the_board)
            place_marker(the_board, player2_marker, pos)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Congratulations,Player 2, won the Game")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Its a Draw")
                    break
                else:
                    turn = 'player1'
    if not replay():
        break

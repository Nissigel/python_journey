from termcolor import cprint

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
]

def print_board(board):
    line = '-----+-----+-----'
    print(line)
    for row in board:
        print(f'  {row[0]}   |   {row[1]}  | {row[2]} ')
        print(line)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return True
        
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != '':
            return True

    if board[0][0] == board[1][1] == board[2][2] != '' or \
        board[0][2] == board[1][1] == board[2][0] != '' :
        return True

    return False

def is_full(board):
    for row in board:
        if '' in row:
            return False
        
    return True

def get_position(prompt):
    while True:
        try:
            position = int(input(prompt))
            if position < 0 or position > 2:
                raise ValueError
            return position
        except ValueError:
            cprint ('Invalid input!', 'magenta')
            print()

def get_move(current_player):
    cprint (f"Player {current_player}'s turn", "blue")
    while True:
        row = get_position ('Enter row (0-2): ')
        column = get_position ('Enter column (0-2): ')


        if board[row][column] == '':
            board[row][column] = current_player
            break
        cprint ('The spot is already taken 😶', 'red')
        print ()


def main():

    current_player = 'X'

    print_board(board,)
    print()

    while True:
        get_move(current_player)

        print_board(board)
        print ()

        if check_winner(board):
            cprint (f'Player {current_player} wins!🥳', 'green')
            print ()
            break

        if is_full(board):
            cprint (f'Board is full!🥱', 'yellow')
            print ()
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()
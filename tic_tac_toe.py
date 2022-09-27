"""
Darien Weller
Project: tic_tac_toe


"""


def main():
    print("Welcome to Tic-Tac-Toe!")
    game_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn = ""
    victory = False
    tie_game = False
    while not (victory or tie_game):
        draw_board(game_board)
        victory = check_victory(game_board)
        if victory:
            print(f"The {turn}'s win!")
            break
        tie_game = check_tie(game_board)
        if tie_game:
            print("Tie Game.")
        turn = switch_player(turn)
        choice = int(input(f"{turn}'s turn to choose a square (1-9): "))
        update_board(game_board, choice, turn)


def draw_board(board):
    print(f"""    
    {board[0]}|{board[1]}|{board[2]}
    -+-+-
    {board[3]}|{board[4]}|{board[5]}
    -+-+-
    {board[6]}|{board[7]}|{board[8]}
    """)


def update_board(board, choice, turn):
    choice -= 1
    board[choice] = turn


def switch_player(player):
    if player == "x":
        return "o"
    else:
        return "x"


def check_victory(board):
    if ((board[8] == board[4] == board[0]) or
            (board[6] == board[4] == board[2]) or
            (board[0] == board[1] == board[2]) or
            (board[3] == board[4] == board[5]) or
            (board[6] == board[7] == board[8]) or
            (board[0] == board[3] == board[6]) or
            (board[1] == board[4] == board[7]) or
            (board[2] == board[5] == board[8])):
        return True
    else:
        return False


def check_tie(board):
    for num in board:
        if num != "x" and num != "o":
            return False
    return True


if __name__ == "__main__":
    main()

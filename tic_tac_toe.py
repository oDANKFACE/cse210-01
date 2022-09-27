"""
Darien Weller
Project: tic_tac_toe


"""


def main():
    game_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn = ""
    victory = False
    tie_game = False
    while not (victory or tie_game):
        draw_board(game_board)
        # check_victory()
        # if victory:
        #     print(f"Great job {turn}'s, you win!")
        #     break
        # check_tie()
        # if tie_game:
        #     print("Tie Game. You're both losers.")
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


def check_victory():
    pass


def check_tie():
    pass


if __name__ == "__main__":
    main()

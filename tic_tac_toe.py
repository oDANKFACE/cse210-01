"""
Darien Weller
Project: tic_tac_toe


"""


def main():
    game_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Hello")
    turn = ""
    victory = False
    tie_game = False
    while not (victory or tie_game):
        draw_board()
        check_victory()
        if victory:
            print(f"Great job {turn}'s, you win!")
            break
        check_tie()
        if tie_game:
            print("Tie Game. You're both losers.")
        switch_player()
        choice = int(input(f"{turn}'s turn to choose a square (1-9): "))
        update_board()


def draw_board():
    pass


def update_board():
    pass


def switch_player():
    pass


def check_victory():
    pass


def check_tie():
    pass


if __name__ == "__main__":
    main()

# TicTacToe by SOLN4R
# version 1.0: 26.11.2024 - 27.11.2024

import random

def print_rules() -> None:
    """ Displays welcome message, rules, and instructions for Tic Tac Toe. """
    print("Welcome to Tic Tac Toe!")
    print("Here are the rules:")
    print("1. The game is played on a grid of 3x3.")
    print("2. Players take turns to place their marks (X or O) in an empty cell.")
    print("3. The first player to align three marks in a row, column, or diagonal wins!")
    print("4. If all cells are filled and no one has three in a row, the game ends in a draw.")
    print("\nGrid positions are numbered as follows:")
    print("  1 | 2 | 3")
    print("  ---------")
    print("  4 | 5 | 6")
    print("  ---------")
    print("  7 | 8 | 9")
    print("\nLet's begin! Good luck!")

def print_field(board, current_move) -> None:
    """ Displays the current game board. """
    print(f"{current_move} make move:\n")
    print(f"\t\t{board[0]} | {board[1]} | {board[2]}")
    print("\t\t" + "-" * 9)
    print(f"\t\t{board[3]} | {board[4]} | {board[5]}")
    print("\t\t" + "-" * 9)
    print(f"\t\t{board[6]} | {board[7]} | {board[8]}")
    print("")

def get_player_mark() -> str:
    """ Asks the player to choose their mark (X or O). """
    while True:
        try:
            user_input = input("Please choose your mark (X or O): ").strip().upper()
            if len(user_input) != 1 or user_input not in ("X", "O"):
                raise ValueError("Invalid input. Enter 'X' or 'O'.")
            return user_input
        except ValueError as e:
            print(f"Error: {e}")

def play_game() -> None:
    """ Main game loop. """
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    player_mark = get_player_mark()
    if player_mark == "X": computer_mark = "O"
    else: computer_mark = "X"
    current_move = "X"
    game_status = True

    while game_status:
        board = make_move(current_move, player_mark, computer_mark, board)
        print_field(board, current_move)
        game_status = check_winner(board)

        if game_status:
            current_move = swap_movement(current_move)

def make_move(current_move, player_mark, computer_mark, board) -> str:
    """ Handle the current player's move. """
    if current_move == player_mark:

        while True:
            user_input = input("Enter your move (1-9): ").strip()
            try:
                move = int(user_input)
                if 1 <= move <= 9 and board[move - 1] == "-":
                    board[move - 1] = current_move
                    return board
                else:
                    print("Invalid move. Slot is either blocked or out of range!")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
    else:
        while True:
            computer_move = random.randrange(0, 9)
            if board[computer_move] == "-":
                board[computer_move] = computer_mark
                return board

def swap_movement(current_move) -> str:
    """ Switch turns between players. """
    return "O" if current_move == "X" else "X"

def check_winner(board) -> bool:
    """ Check the board for a winner or a draw. """
    if board[0] == board[1] == board[2] and board[0] != "-":
        print(f"Game Over: {board[0]} wins!")
        return False
    elif board[3] == board[4] == board[5] and board[3] != "-":
        print(f"Game over: {board[3]} Win!")
        return False
    elif board[6] == board[7] == board[8] and board[6] != "-":
        print(f"Game over: {board[6]} Win!")
        return False

    elif board[0] == board[3] == board[6] and board[0] != "-":
        print(f"Game over: {board[0]} Win!")
        return False
    elif board[1] == board[4] == board[7] and board[1] != "-":
        print(f"Game over: {board[1]} Win!")
        return False
    elif board[2] == board[5] == board[8] and board[2] != "-":
        print(f"Game over: {board[2]} Win!")
        return False

    elif board[0] == board[4] == board[8] and board[0] != "-":
        print(f"Game over: {board[0]} Win!")
        return False
    elif board[2] == board[4] == board[6] and board[2] != "-":
        print(f"Game over: {board[2]} Win!")
        return False

    for item in board:
        if item == "-": return True

    print("Game over: It's a draw!")
    return False

def main() -> None:
    """ Start the game. """
    print_rules()
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
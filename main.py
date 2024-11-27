# TicTacToe by SOLN4R
# version 1.0 (Initial version): 26.11.2024 - 27.11.2024
# version 1.1 (Minimax integration): 27.11.2024

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
    print(f"\t\t{board[0]} | {board[1]} | {board[2]} \t\t1 | 2 | 3")
    print("\t\t" + "-" * 9 + "\t\t---------")
    print(f"\t\t{board[3]} | {board[4]} | {board[5]} \t\t4 | 5 | 6")
    print("\t\t" + "-" * 9 + "\t\t---------")
    print(f"\t\t{board[6]} | {board[7]} | {board[8]} \t\t7 | 8 | 9")
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

def evaluate(board, computer_mark, player_mark):
    """ Evaluate the current state of the board. """
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]]:
            if board[condition[0]] == computer_mark:
                return 10
            elif board[condition[0]] == player_mark:
                return -10
    return 0

def minimax(board, depth, is_maximizing, computer_mark, player_mark):
    """ Minimax algorithm to find the optimal move. """
    score = evaluate(board, computer_mark, player_mark)
    if score == 10 or score == -10:
        return score
    if "-" not in board:
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == "-":
                board[i] = computer_mark
                best_score = max(best_score, minimax(board, depth + 1, False, computer_mark, player_mark))
                board[i] = "-"
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == "-":
                board[i] = player_mark
                best_score = min(best_score, minimax(board, depth + 1, True, computer_mark, player_mark))
                board[i] = "-"
        return best_score

def best_move(board, computer_mark, player_mark):
    """ Find the best move for the computer. """
    best_score = -float("inf")
    move = -1
    for i in range(9):
        if board[i] == "-":
            board[i] = computer_mark
            score = minimax(board, 0, False, computer_mark, player_mark)
            board[i] = "-"
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game() -> None:
    """ Main game loop. """
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    player_mark = get_player_mark()
    computer_mark = "O" if player_mark == "X" else "X"
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
        move = best_move(board, computer_mark, player_mark)
        if move != -1:
            board[move] = computer_mark
        return board

def swap_movement(current_move) -> str:
    """ Switch turns between players. """
    return "O" if current_move == "X" else "X"

def check_winner(board) -> bool:
    """ Check the board for a winner or a draw. """
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != "-":
            print(f"Game Over: {board[condition[0]]} wins!")
            return False
    if "-" not in board:
        print("Game Over: It's a draw!")
        return False
    return True

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

import tkinter as tk
from tkinter import messagebox

# Check if there are any empty spaces left on the board
def has_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

# Check for a winner and return a score
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return 10 if row[0] == "X" else -10

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return 10 if board[0][col] == "X" else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 10 if board[0][0] == "X" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 10 if board[0][2] == "X" else -10

    # No winner yet
    return 0

# Minimax algorithm to calculate the best move
def minimax(board, depth, is_max, alpha, beta):
    score = check_winner(board)

    if score == 10 or score == -10:
        return score

    if not has_moves_left(board):
        return 0

    if is_max:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best_score = max(best_score, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = " "
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best_score = min(best_score, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = " "
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

# Decide the best move for the AI
def get_best_move(board):
    best_score = float('-inf')
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move

# Handle button clicks and update the game
def handle_click(buttons, board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        buttons[row][col]["text"] = player

        result = check_winner(board)

        if result == 10:
            messagebox.showinfo("Game Over", "AI wins!")
            reset_game(buttons, board)
        elif result == -10:
            messagebox.showinfo("Game Over", "You win!")
            reset_game(buttons, board)
        elif not has_moves_left(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game(buttons, board)
        elif player == "O":
            ai_move = get_best_move(board)
            handle_click(buttons, board, ai_move[0], ai_move[1], "X")

# Reset the game to its initial state
def reset_game(buttons, board):
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
            buttons[i][j]["text"] = " "

# Main function to create the game window and start the game
def main():
    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    board = [[" " for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text=" ", font=("Arial", 24), height=2, width=5,
                                      command=lambda r=i, c=j: handle_click(buttons, board, r, c, "O"))
            buttons[i][j].grid(row=i, column=j)

    root.mainloop()

if __name__ == "__main__":
    main()

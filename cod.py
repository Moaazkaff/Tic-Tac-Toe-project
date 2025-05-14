import tkinter as tk
from tkinter import messagebox
import random
import copy

class Board:
    def __init__(self):
        self.cells = [" "] * 10

    def update_cell(self, i, player):
        if self.cells[i] == " ":
            self.cells[i] = player
            return False
        return True

    def evaluation(self):
        for i in range(1 , 7 , 3):
            if self.cells[i] == self.cells[i+1] == self.cells[i+2] == "X":
                return +10
            if self.cells[i] == self.cells[i+1] == self.cells[i+2] == "O":
                return -10
        for i in range(1 , 4):
            if self.cells[i] == self.cells[i+3] == self.cells[i+6] == "X":
                return +10
            if self.cells[i] == self.cells[i+3] == self.cells[i+6] == "O":
                    return -10
        if self.cells[1] == self.cells[5] == self.cells[9] == "X":
                return +10
        if self.cells[1] == self.cells[5] == self.cells[9] == "O":
            return -10
        if self.cells[3] == self.cells[5] == self.cells[7] == "X":
            return +10
        if self.cells[3] == self.cells[5] == self.cells[7] == "O":
            return -10
        return 0

    def get_empty_cells(self):
        return [i for i in range(1, 10) if self.cells[i] == " "]

    def is_draw(self):
        return " " not in self.cells[1:]

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk() # Create the main window
        self.window.title("Tic Tac Toe") # title 
        self.mode = None # mode
        self.board = Board() 
        self.current_player = "X" # 
        self.buttons = {}

        self.main_menu()

        self.window.mainloop()

    def main_menu(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        tk.Label(self.window, text="Choose Game Mode:", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.window, text="Player vs Player", width=25, height=2, font=("Arial", 14),
            command=lambda: self.start_game("PVP")).pack(pady=5)

        tk.Button(self.window, text="Player vs AI (Easy)", width=25, height=2, font=("Arial", 14),
            command=lambda: self.start_game("EASY")).pack(pady=5)

        tk.Button(self.window, text="Player vs AI (Hard)", width=25, height=2, font=("Arial", 14),
            command=lambda: self.start_game("HARD")).pack(pady=5)

        tk.Button(self.window, text="Quit", width=25, height=2, font=("Arial", 14),
            command=self.window.quit, bg="red", fg="white").pack(pady=10)

    def start_game(self, mode):
        self.mode = mode
        self.board = Board()
        self.current_player = "X"

        for widget in self.window.winfo_children():
            widget.destroy()

        self.status_label = tk.Label(self.window, text="Player X's turn", font=("Arial", 16))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=10)

        for i in range(1, 10):
            btn = tk.Button(self.window, text=" ", font=("Arial", 32), width=5, height=2,
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=(i - 1) // 3 + 1, column=(i - 1) % 3)
            self.buttons[i] = btn

    def on_click(self, pos):
        if self.board.cells[pos] != " ":
            return

        self.board.update_cell(pos, self.current_player)
        self.buttons[pos]["text"] = self.current_player

        if self.check_end():
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(text=f"Player {self.current_player}'s turn")

        if self.mode in ("EASY", "HARD") and self.current_player == "O":
            self.window.after(500, self.ai_move)

    def ai_move(self):
        if self.mode == "EASY":
            move = random.choice(self.board.get_empty_cells())
        else:
            move = self.best_move()

        self.board.update_cell(move, "O")
        self.buttons[move]["text"] = "O"

        if self.check_end():
            return

        self.current_player = "X"
        self.status_label.config(text="Player X's turn")

    def check_end(self):
        score = self.board.evaluation()
        if score == 10:
            self.end_game("Player X wins!")
            return True
        elif score == -10:
            self.end_game("Player O wins!")
            return True
        elif self.board.is_draw():
            self.end_game("It's a draw!")
            return True
        return False

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.ask_play_again()

    def ask_play_again(self):
        if messagebox.askyesno("Play Again?", "Do you want to play another round?"):
            self.start_game(self.mode)
        else:
            self.main_menu()

    def minmax(self, board, depth, is_max, alpha, beta):
        score = board.evaluation()
        if score != 0 or board.is_draw():
            return score

        if is_max:
            best = -float('inf')
            for i in board.get_empty_cells():
                board.cells[i] = "X"
                val = self.minmax(board, depth + 1, False, alpha, beta)
                board.cells[i] = " "
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return best
        else:
            best = float('inf')
            for i in board.get_empty_cells():
                board.cells[i] = "O"
                val = self.minmax(board, depth + 1, True, alpha, beta)
                board.cells[i] = " "
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
            return best

    def best_move(self):
        best_val = float('inf')
        move = -1
        for i in self.board.get_empty_cells():
            self.board.cells[i] = "O"
            move_val = self.minmax(copy.deepcopy(self.board), 0, True, -float("inf"), float("inf"))
            self.board.cells[i] = " "
            if move_val < best_val:
                best_val = move_val
                move = i
        return move
if __name__ == "__main__":
    TicTacToeGUI()
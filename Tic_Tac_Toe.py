import os
import random
os.system("cls")


class Board:
    def __init__(self):
        self.cells = [" "] * 10

    def display(self):
        print((f" {self.cells[1]} | {self.cells[2]} | {self.cells[3]} "))
        print("-----------")
        print((f" {self.cells[4]} | {self.cells[5]} | {self.cells[6]} "))
        print("-----------")
        print((f" {self.cells[7]} | {self.cells[8]} | {self.cells[9]} "))
        print()

    def update_cell(self , cell_number, player):
        if self.cells[cell_number] == " ":
            self.cells[cell_number] = player
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
    
    # evaluation function using winning combinations
    # def evaluation(self):
    #     winning_combos = [
    #     (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
    #     (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
    #     (1, 5, 9), (3, 5, 7)              # Diagonals
    # ]
    #     for a, b, c in winning_combos:
    #         if self.cells[a] == self.cells[b] == self.cells[c] == "X":
    #             return 10
    #         elif self.cells[a] == self.cells[b] == self.cells[c] == "O":
    #             return -10
    #     return 0


        
        

board = Board()

def print_header():
    print("Welcome to Tic Tac Toe game!\n")


def refresh_board():
    # clear the console
    os.system("cls")

    # print the header
    print_header()

    # print the board
    board.display()

def Check_winner():
    check = board.evaluation()

    if check == 10:
        print("Player X wins!")
        return True
    elif check == -10:
        print("Player O wins!")
        return True
    if " " not in board.cells[1:]:
        print("It's a draw!")
        return True
    return False

def get_valid_choice(player):
    while True:
        try:
            choice = int(input(f"Player {player}, choose a cell (1 -> 9): "))
            refresh_board()
            if 1 <= int(choice) <= 9:
                return int(choice)
            print("Invalid choice! Please choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter a number.")





def get_empty_cell(board):
    return [i for i in range(1 , 10) if board.cells[i] == " "]

def minmax(board , depth , is_Maximizing , alpha , beta):
    # minmax using alpha and beta purnning

    score = board.evaluation()

    if score == 10 or score == -10 or " " not in board.cells[1:]:
        return score
    if is_Maximizing:
        max_eval = -float("inf")
        for i in get_empty_cell(board):
            board.cells[i] = "X"
            eval = minmax(board , depth + 1 , False , alpha , beta)
            board.cells[i] = " "
            max_eval = max(max_eval , eval)
            alpha = max(alpha , max_eval)
            if alpha >= beta:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for i in get_empty_cell(board):
            board.cells[i] = "O"
            eval = minmax(board , depth + 1 , True , alpha , beta)
            board.cells[i] = " "
            min_eval = min(min_eval , eval)
            beta = min(beta , min_eval)
            if alpha >= beta:
                break
        return min_eval

def best_move(board):
    best_val = float("inf")
    best_move = -1
    for i in get_empty_cell(board):
        board.cells[i] = "O"
        move_val = minmax(board , 0 , True , -float("inf") , float("inf"))
        board.cells[i] = " "
        if move_val < best_val:
            best_val = move_val
            best_move = i
    return best_move




# 1 Vs 1 Function
def player_vs_player():
    
    while True:
    # refresh the board
        refresh_board()

    # get the X choice
    # x_choice = int(input("Player X, choose a cell (1 -> 9): ")) 
        x_choice = get_valid_choice("X")

    # update the board with X
        while board.update_cell(x_choice, "X"):
            refresh_board()
            print("Cell already taken! Choose another cell.")
            x_choice = get_valid_choice("X")

    # refresh the board
        refresh_board()

    # check for winner
        if Check_winner():
            break

    # get the O choice
    # o_choice = int(input("Player O, choose a cell (1 -> 9): ")) 
        o_choice = get_valid_choice("O")

    # update the board with O
        while board.update_cell(o_choice, "O"):
            refresh_board()
            print("Cell already taken! Choose another cell.")
            o_choice = get_valid_choice("O")
    
    # refresh the board
        refresh_board()
    
    # check for winner
        if Check_winner():
            break


def player_vs_ai_easy():
    while True:
        refresh_board()

        # Get the player's move (X)
        x_choice = get_valid_choice("X")
        while board.update_cell(x_choice, "X"):
            refresh_board()
            print("Cell already taken! Choose another cell.")
            x_choice = get_valid_choice("X")

        refresh_board()
        if Check_winner():
            break

        # AI move (O)
        available_cells = [i for i in range(1, 10) if board.cells[i] == " "]
        if not available_cells:
            break
        o_choice = random.choice(available_cells)
        board.update_cell(o_choice, "O")

        refresh_board()
        if Check_winner():
            break


def player_vs_ai_hard():
    while True:
        refresh_board()

        # Get the player's move (X)
        x_choice = get_valid_choice("X")
        while board.update_cell(x_choice, "X"):
            refresh_board()
            print("Cell already taken! Choose another cell.")
            x_choice = get_valid_choice("X")

        refresh_board()
        if Check_winner():
            break

        # AI move (O)
        ai_move = best_move(board)
        if ai_move == -1:
            break # Tie
        board.update_cell(ai_move , "O")

        refresh_board()

        if Check_winner():
            break
        


def game_mode():
    print("Welcome to Tic Tac Toe!")
    print("Choose your game mode:")
    print("1. Player vs Player")
    print("2. Player vs AI (Easy)")
    print("3. Player vs AI (Hard)")

    game_mode = int(input("Enter your choice (1-3): "))

    if game_mode == 1:
        print("You chose Player vs Player mode.")
        # Call the function for player vs player
        player_vs_player()

    elif game_mode == 2:
        print("You chose Player vs AI (Easy) mode.")
        player_vs_ai_easy()

    elif game_mode == 3:
        print("You chose Player vs AI (Hard) mode.")
        # Call the function for player vs AI (Easy)
        player_vs_ai_hard()

    else:
        print("Invalid choice!")



def main():
    while True:
        global board
        board = Board()
        game_mode()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()






    
# print("Welcome to Tic Tac Toe!")
# print("Choose your game mode:")
# print("1. Player vs Player")
# print("2. Player vs AI (Easy)")
# print("3. Player vs AI (Hard)")


# game_mode = int(input("Enter your choice (1-3): "))

# if game_mode == 1:

#     print("You chose Player vs Player mode.")
#     # Call the function for player vs player
#     player_vs_player()


# elif game_mode == 2:

#     print("You chose Player vs AI (Easy) mode.")
#     # Call the function for player vs AI (Easy)
#     pass


# elif game_mode == 3:

#     print("You chose Player vs AI (Hard) mode.")
#     # Call the function for player vs AI (Easy)
#     pass

# else:
#     print("Invalid choice!")


# while True:
#     # refresh the board
#     refresh_board()

#     # get the X choice
#     # x_choice = int(input("Player X, choose a cell (1 -> 9): ")) 
#     x_choice = get_valid_choice("X")

#     # update the board with X
#     while board.update_cell(x_choice, "X"):
#         refresh_board()
#         print("Cell already taken! Choose another cell.")
#         x_choice = get_valid_choice("X")

#     # refresh the board
#     refresh_board()

#     # check for winner
#     if Check_winner():
#         break

#     # get the O choice
#     # o_choice = int(input("Player O, choose a cell (1 -> 9): ")) 
#     o_choice = get_valid_choice("O")

#     # update the board with O
#     while board.update_cell(o_choice, "O"):
#         refresh_board()
#         print("Cell already taken! Choose another cell.")
#         o_choice = get_valid_choice("O")
    
#     # refresh the board
#     refresh_board()
    
#     # check for winner
#     if Check_winner():
#         break

    
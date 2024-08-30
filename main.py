import tkinter as tk
from tkinter import messagebox

def check_win():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
         return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

def check_draw():
    for row in board:
        if "" in row:
            return False
    return True

def button_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "" and current_player:
        buttons[row][col]["text"] = current_player
        board[row][col] = current_player
        if check_win():
            messagebox.showinfo("Oyun Bitti", f"Oyuncu {current_player} kazandı!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Oyun Bitti", "Berabere!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            board[row][col] = ""

root = tk.Tk()
root.title("XOXO Oyunu")

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        button = tk.Button(root, text="", font='normal 20 bold', width=5, height=2,
                           command=lambda row=row, col=col: button_click(row, col))
        button.grid(row=row, column=col)
        buttons[row][col] = button

root.mainloop()
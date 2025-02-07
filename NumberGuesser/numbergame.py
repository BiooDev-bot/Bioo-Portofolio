import tkinter as tk
from tkinter import messagebox
import random

# Initialize data
attempt_datasave = []
number_guessed = []
history_log = []
life_data = []
diff_data = []

lose = 0
win = 0
match_log = 0
tebak_angka = 0
angka_tebak = ""
attempt_s = 0
life_bar = 0
diff = ""

# Functions
def reset_game():
    global tebak_angka, angka_tebak, attempt_s, life_bar, diff
    tebak_angka = 0
    angka_tebak = ""
    attempt_s = 0
    life_bar = 0
    diff = ""

def start_game(difficulty):
    global tebak_angka, angka_tebak, attempt_s, life_bar, diff
    attempt_s = 0
    if difficulty == "Easy":
        tebak_angka = random.randint(0, 100)
        angka_tebak = "0-100"
        life_bar = 20
    elif difficulty == "Medium":
        tebak_angka = random.randint(0, 100)
        angka_tebak = "0-100"
        life_bar = 15
    elif difficulty == "Hard":
        tebak_angka = random.randint(0, 150)
        angka_tebak = "0-150"
        life_bar = 10
    elif difficulty == "Professional":
        tebak_angka = random.randint(0, 150)
        angka_tebak = "0-150"
        life_bar = 10
    elif difficulty == "Legend":
        tebak_angka = random.randint(0, 150)
        angka_tebak = "0-150"
        life_bar = 5
    
    diff = difficulty
    diff_data.append(diff)
    lbl_status.config(text=f"Number is between {angka_tebak}. You have {life_bar} attempts. Good luck!")
    entry_guess.delete(0, tk.END)

def check_guess(event=None):
    global attempt_s, life_bar, lose, win, match_log
    if tebak_angka == 0:
        messagebox.showwarning("Warning", "Start a game first!")
        return

    try:
        guess = int(entry_guess.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    attempt_s += 1
    if guess == tebak_angka:
        messagebox.showinfo("Congratulations", f"Correct! You guessed it in {attempt_s} attempts.")
        save_game_data("WIN")
        reset_game()
        lbl_status.config(text="You won! Start a new game.")
    else:
        if abs(guess - tebak_angka) < 10:
            hint = "Close, but too high!" if guess > tebak_angka else "Close, but too low!"
        elif guess > tebak_angka:
            hint = "Too high!"
        else:
            hint = "Too low!"

        life_bar -= 1
        lbl_status.config(text=f"{hint} Attempts left: {life_bar}")

        if life_bar == 0:
            messagebox.showinfo("Game Over", f"You lost! The correct number was {tebak_angka}.")
            save_game_data("LOSE")
            reset_game()
            lbl_status.config(text="You lost! Start a new game.")

def save_game_data(result):
    global match_log, lose, win
    attempt_datasave.append(attempt_s)
    number_guessed.append(tebak_angka)
    history_log.append(result)
    life_data.append(life_bar)
    match_log += 1

    if result == "WIN":
        win += 1
    else:
        lose += 1

def show_history():
    if match_log == 0:
        messagebox.showinfo("No History", "You haven't played any games yet.")
        return

    history_text = ""
    for i in range(match_log):
        history_text += (f"Game {i+1}: Result: {history_log[i]}, Difficulty: {diff_data[i]}, Guesses: {attempt_datasave[i]}, Number: {number_guessed[i]}\n")
    
    messagebox.showinfo("Game History", history_text)

# GUI setup
root = tk.Tk()
root.title("Tebak Angka")
root.geometry("400x500+400+90")
root.configure(bg="#f0f8ff")

# Widgets
lbl_title = tk.Label(root, text="=== Tebak Angka ===", font=("Arial", 16, "bold"), bg="#4682b4", fg="white", pady=10)
lbl_title.pack(fill=tk.X)

frame_controls = tk.Frame(root, bg="#f0f8ff")
frame_controls.pack(pady=10)

btn_easy = tk.Button(frame_controls, text="Easy", command=lambda: start_game("Easy"), bg="#90ee90", font=("Arial", 12))
btn_easy.grid(row=0, column=0, padx=5)

btn_medium = tk.Button(frame_controls, text="Medium", command=lambda: start_game("Medium"), bg="#add8e6", font=("Arial", 12))
btn_medium.grid(row=0, column=1, padx=5)

btn_hard = tk.Button(frame_controls, text="Hard", command=lambda: start_game("Hard"), bg="#ffa07a", font=("Arial", 12))
btn_hard.grid(row=0, column=2, padx=5)

btn_professional = tk.Button(frame_controls, text="Professional", command=lambda: start_game("Professional"), bg="#ffdab9", font=("Arial", 12))
btn_professional.grid(row=0, column=3, padx=5)

btn_legend = tk.Button(frame_controls, text="Legend", command=lambda: start_game("Legend"), bg="#ff6347", font=("Arial", 12))
btn_legend.grid(row=0, column=4, padx=5)

lbl_status = tk.Label(root, text="Select a difficulty to start.", bg="#f0f8ff", font=("Arial", 12))
lbl_status.pack(pady=10)

frame_guess = tk.Frame(root, bg="#f0f8ff")
frame_guess.pack(pady=10)

entry_guess = tk.Entry(frame_guess, font=("Arial", 14))
entry_guess.grid(row=0, column=0, padx=5)

btn_guess = tk.Button(frame_guess, text="Guess", command=check_guess, bg="#87ceeb", font=("Arial", 12))
btn_guess.grid(row=0, column=1, padx=5)

btn_history = tk.Button(root, text="Show History", command=show_history, bg="#4682b4", fg="white", font=("Arial", 12))
btn_history.pack(pady=5)

btn_exit = tk.Button(root, text="Exit", command=root.quit, bg="#ff4500", fg="white", font=("Arial", 12))
btn_exit.pack(pady=5)

# Key bindings
root.bind("<Return>", check_guess)

# Run application
reset_game()
root.mainloop()

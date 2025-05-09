import tkinter as tk
import random

# Global score
user_score = 0
computer_score = 0

# Game logic
def play(user_choice):
    global user_score, computer_score

    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Scissors' and computer_choice == 'Paper') or
        (user_choice == 'Paper' and computer_choice == 'Rock')
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x350")
root.resizable(False, False)

# Heading
tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14)).pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(button_frame, text="Rock", width=10, command=lambda: play('Rock')).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play('Paper')).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play('Scissors')).grid(row=0, column=2, padx=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Score tracking
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Exit button
tk.Button(root, text="Exit Game", command=root.destroy, fg="white", bg="red", font=("Arial", 10)).pack(pady=10)

# Start GUI loop
root.mainloop()

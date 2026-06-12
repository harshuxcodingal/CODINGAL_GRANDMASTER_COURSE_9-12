import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(
        text=f"You: {user_choice}\nComputer: {computer_choice}\n\n{result}"
    )

# Create Window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

# Heading
title = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16))
title.pack(pady=10)

# Buttons
rock_btn = tk.Button(root, text="Rock", width=15,
                     command=lambda: play("Rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(root, text="Paper", width=15,
                      command=lambda: play("Paper"))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(root, text="Scissors", width=15,
                         command=lambda: play("Scissors"))
scissors_btn.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Run Window
root.mainloop()
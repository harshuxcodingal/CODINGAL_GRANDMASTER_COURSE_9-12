import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Enter rock, paper, or scissors: ").lower()

print("Computer chose:", computer)

if user == computer:
    print("It's a Tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You Win!")
else:
    print("Computer Wins!")
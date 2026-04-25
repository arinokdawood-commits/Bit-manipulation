import random

choices = ["rock", "paper", "scissors"]
c = random.choice(choices)
u = input("rock/paper/scissors: ").lower()

if u not in choices:
    print("Invalid choice")
elif u == c:
    print("Tie")
elif (u == "rock" and c == "scissors") or \
     (u == "paper" and c == "rock") or \
     (u == "scissors" and c == "paper"):
    print("You Win!")
else:
    print("You Lose! Computer chose", c)
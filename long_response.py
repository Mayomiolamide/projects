import random
print("...Welcome to the rock paper scissors game...")
while True:
    choice = "rock", "paper", "scissors"
    Guess = random.choice(choice)
    Game = input("Please Choose: ").lower()
    if Game == "scissors" and Guess == "rock":
        print("You loose")
    elif Game == "scissors" and Guess == "paper":
        print("You won!!")
    elif Game == "rock" and Guess == "scissors":
        print("You won!!")
    elif Game == "rock" and Guess == "paper":
        print("You loose")
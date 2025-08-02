#number Guessing project in python.........
import random
print("-----This is a number guessing game-----")
print("--------Guess a number from 1:10--------")
while True:
    Guess = random.randint(1,10)
    while True:
        try:
            prompt = int(input("guess👀:"))
            if prompt < Guess:
                print("too low, guess higher")
            elif prompt > Guess:
                print("too high, guess lower")
            elif prompt == Guess:
                print("Congratulations you won!!!🌟")
                break
        except ValueError:
            print("Enter a number between 1:10🤦‍♀️")
    while True:
        play_again = input("Do you want to play again(y/n):").lower()
        if play_again == "y":
            break
        elif play_again == "n":
            print("thanks for playing, GOODBYE!!👍")
            exit()
        else:
            print("Enter a valid input, (y/n)")


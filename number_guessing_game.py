import random
import art

def select_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return 10
    else:
        return 5
def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = select_difficulty()
    number = random.randint(1, 100)

    while attempts>0:
            print(f"\nYou have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))

            if number > guess:
                if attempts==1:
                    print("Too low")
                else:
                    print("Too low.\nGuess again.")
            elif number < guess:
                if attempts==1:
                    print("Too high")
                else:
                    print("Too high.\nGuess again.")
            else:
                print(f"\nYou got it. The number was {number}.YOU WIN!!!\n")
                again=input("Do you want to play again? Type 'yes' or 'no'. ").lower()
                if again=="yes":
                    print("\n"*20)
                    game()
                else:
                    break
            attempts -= 1

            if attempts==0:
                print(f"\nGAME OVER!!! You've run out of guesses. The number was {number}.\n")
                again=input("Do you want to play again? Type 'yes' or 'no'. ").lower()
                if again=="yes":
                    print("\n"*20)
                    game()

game()
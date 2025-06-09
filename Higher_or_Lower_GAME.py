from random import randint
from art import logo,vs
from game_data import data

def random_index():
    return randint(0,len(data))

def game():
    score=0

    n_A=random_index()
    n_B=random_index()
    while n_B == n_A:
        n_B=random_index()

    game_continue=True
    while game_continue:
        a_followers=data[n_A]['follower_count']
        b_followers=data[n_B]['follower_count']
        print(logo)
        print(f"Compare A: {data[n_A]['name']}, a {data[n_A]['description']}, from {data[n_A]['country']}.")
        print(vs)
        print(f"Compare B: {data[n_B]['name']}, a {data[n_B]['description']}, from {data[n_B]['country']}.")
        guess=input("\nWho has more followers? Type 'A' or 'B': ").lower()

        if (guess=='a' and a_followers>b_followers) or (guess=='b' and b_followers>a_followers):
            score += 1
            print(f"\nYou're right! Current score: {score}\n\n")
            n_A=n_B
            n_B=random_index()
            while n_B==n_A:
                n_B=random_index()
        else:
            print(f"\nSorry. That's wrong. Final score: {score}\n\n")
            wanna_play=input("\nDo you want to play again? Type 'y' or 'n': ").lower()
            if wanna_play=='y':
                game()
            else:
                game_continue=False
game()
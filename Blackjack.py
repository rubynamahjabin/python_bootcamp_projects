#Welcome to the Blackjack game! Get ready to play against the computer.
#Both you and the computer start with two cards drawn randomly.
#Cards are valued as follows:
#Numbers 2–10 are worth their face value.
#J,Q,K are worth 10
#Ace(A) can be 11 or 1, depending on which keeps the total score ≤ 21
#A starting hand of two cards totaling 21 is a Blackjack and wins immediately (unless both get it, which is a draw).
#You’ll see your cards and the computer’s first card.
#On your turn, you can choose to draw another card ("y") or pass ("n").
#If your score goes over 21, you lose immediately.
#After your turn, the computer draws more cards until its score is 17 or higher or it gets a Blackjack.
#Final scores are compared and a result message is displayed: win, lose, draw, or special cases like Blackjack.

import art
import random

def deal_card():
    """returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score"""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_Game_Over=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_Game_Over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_Game_Over=True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                is_Game_Over=True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()=="y":
    print("\n"*20)
    play_game()
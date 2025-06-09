import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def game():
    choice=int(input("\nWhat do you choose? Type 0 for rock,1 for paper,2 for scissors.\n"))

    if choice==0:
        print(rock)
    elif choice==1:
        print(paper)
    elif choice==2:
        print(scissors)

    print("Computer chose:")
    computer=random.randint(0,2)
    if computer==0:
        print(rock)
    elif computer==1:
        print(paper)
    elif computer==2:
        print(scissors)

    if computer==choice:
        print("It's a draw")
    elif choice==0 and computer==1:
        print("You lose")
    elif choice==0 and computer==2:
        print("You win!")
    elif choice==1 and computer==0:
        print("You win!")
    elif choice==1 and computer==2:
        print("You lose")
    elif choice==2 and computer==0:
        print("You lose")
    elif choice==2 and computer==1:
        print("You win!")
    else:
        print("Invalid input.You lose!")

    play_again=input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again=='y':
        print("\n"*20)
        game()

game()
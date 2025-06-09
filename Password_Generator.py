from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to Password Generator!")
level=input("Do you want your password to be easy or hard? Type 'e' or 'h':\n").lower()
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

if level=="e":
    password=""
    for i in range(0,n_letters):
        password+=choice(letters)
    for i in range(0,n_symbols):
        password+=choice(symbols)
    for i in range(0,n_numbers):
        password+=choice(numbers)
    print(f"\n\nYour password is: {password}")

elif level=="h":
    password=""
    password_list=[]
    for i in range(0,n_letters):
        password_list.append(choice(letters))
    for i in range(0,n_symbols):
        password_list.append(choice(symbols))
    for i in range(0, n_numbers):
        password_list.append(choice(numbers))
    shuffle(password_list)
    for i in range(0,len(password_list)):
        password+=password_list[i]
    print(f"\n\nYour password is: {password}")
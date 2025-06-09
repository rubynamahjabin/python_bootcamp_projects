print("Welcome to Python Pizza Deliveries!")

#Taking order from customer
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill = 0
#Pizza costs $15 for small size, $20 for medium size and $25 for large size
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("You have chosen an invalid size.")
#If customer wants pepperoni, he has to pay extra $2 for small size and $3 for medium or large size
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
#For extra cheese, extra $1 is needed to pay for any size pizza
if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")
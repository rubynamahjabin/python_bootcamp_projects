#try...except block is used to handle errors gracefully.
#By using this you can show user what went wrong instead of crashing the program.

try:
    age = int(input("How old are you? "))
except ValueError:
    print("INVALID input.Try with a numeric response such as 20")
    age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")

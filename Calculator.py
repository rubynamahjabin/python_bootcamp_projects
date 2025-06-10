import art

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    print(art.logo)
    continue_calculating=True

    first_number = float(input("What's the first number? "))

    while continue_calculating:
        for symbol in operations:
            print(symbol)
        op = input("Pick an operation: ")
        second_number = float(input("What's the next number? "))
        result=operations[op](first_number,second_number)
        print(f"{first_number}{op}{second_number}={result}")
        choice=input(f"Type 'y' to continue calculating with {result} or"
                                   f" type 'n' to start a new calculation or "
                     f"type 'off' to turn off the calculator: ").lower()
        if choice=="y":
            first_number=result
        elif choice=="n":
            print("\n"*20)
            continue_calculating=False
            calculator()
        elif choice=="off":
            continue_calculating=False
calculator()
#FizzBuzz
#numbers from 1 to 100 are printed
#If the number is divisible by 3, it is replaced with "Fizz"
#If the number is divisible by 5, it is replaced with "Buzz"
#If the number is divisible by 3 as well as 5, it is replaced with "FizzBuzz"
for num in range(1,101):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)
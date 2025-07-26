#**args:Unlimited Positional Arguments
#collects extra positional arguments into a tuple
def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum

print(add(3,5,6,7,6,5,4,6,7))

#**kwargs: Many keyworded arguments
#collects extra positional arguments into a dictionary
def calculate(n,**kwargs):
        n+=kwargs["add"]
        n*=kwargs["multiply"]
        print(n)

calculate(2,add=3,multiply=5)

class Car:

    def __init__(self,**kw):
        self.make=kw.get("make")
        self.model=kw.get("model")

my_car=Car(make="Nissan",model="GT-6")
print(my_car.make)
print(my_car.model)
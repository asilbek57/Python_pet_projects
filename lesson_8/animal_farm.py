class Animal:
    def __init__(self, name, age, price, food):
        self.name = name
        self.age = age
        self.price = price
        self.food = food

    def walk(self):
        print(f"{self.name}, the {type(self).__name__.lower()}, walks around your farmhouse happily\n")

    def eat(self):
        print(f"{self.name}, the {type(self).__name__.lower()}, enjoys eating {self.food}\n")

    def info(self):
        print(f"""This {type(self).__name__.lower()}'s name is {self.name}
Being {self.age} years old, it costs ${self.price}
Favourite food of {self.name} is {self.food}\n
""")


class Pig(Animal):
    def __init__(self, name, age, price, food, mushroom):
        super().__init__(name, age, price, food)
        self.mushroom = mushroom

    def search(self):
        print(f"{self.name}, using its great sense, is searching for {self.mushroom} mushroom in the mud beneath the earth\n")

class Horse(Animal):
    def __init__(self, name, age, price, food, speed):
        super().__init__(name, age, price, food)
        self.speed = speed

    def running(self):
        print(f"{self.name} is a powerful runner, being able to run with {self.speed} km in an hour!\n")

class Cow(Animal):
    def __init__(self, name, age, price, food, gallons_of_milk):
        super().__init__(name, age, price, food)
        self.gallons_of_milk = gallons_of_milk

    def milk_production(self):
        print(f"{self.name} can produce {self.gallons_of_milk} gallons of milk per day! A great supply for a farmer!\n")

class Sheep(Animal):
    def __init__(self, name, age, price, food, wool):
        super().__init__(name, age, price, food)
        self.wool = wool

    def wool_production(self):
        print(f"{self.name} can give you {self.wool} pounds of wool per annually! You can convert this wool to textile later!\n")

class Chicken(Animal):
    def __init__(self, name, age, price, food, egg_amount):
        super().__init__(name,age,price,food)
        self.egg_amount = egg_amount

    def egg_production(self):
        print(f"{self.name} can produce {self.egg_amount} eggs per week! Let chicks get born or use eggs for other purposes\n")


pig1 = Pig('Napoleon', 2, 300, 'beans', 'truffle')
horse1 = Horse('Boxer', 7, 10000, 'hay', 20)
cow1 = Cow('Maria', 5, 3400, 'hay', 4)
sheep1 = Sheep('Black Noir', 4, 1000, 'wheat', 15)
chicken1 = Chicken('Josuke', 3, 30, 'corn', 5)

print("Welcome to the Animal Farm, with a great variety in animals! Here they are:\n")

pig1.search()
pig1.eat()
pig1.walk()
pig1.info()

horse1.info()
horse1.running()

cow1.info()
cow1.milk_production()

sheep1.info()
sheep1.wool_production()

chicken1.info()
chicken1.egg_production

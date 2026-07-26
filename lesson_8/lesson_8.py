###TASK 1

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


###TASK 2
class Account:
    def __init__(self, name, account_number, balance = 0):
        self.account_number = account_number
        if not isinstance(name, str) or name == '':
            raise ValueError (f'Your account name cannot be {name}!') 
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.account_number}, {self.name}, {self.balance}"
    
    def to_dict(self):
        return {'Account Number' : self.account_number,
                'Name' : self.name,
                'Balance' : self.balance
                }
import json
class Bank:
    def __init__(self):
        self.num_generator = 1000
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        acc_num = self.num_generator 
        self.num_generator +=1

        acc = Account(name = name, account_number = acc_num, balance= initial_deposit)
        self.accounts[acc_num] = acc
        self.save_to_file()
        print("Account successfully added")

    def view_details(self):
        ask = int(input("Enter the account number to view details"))
        if ask in self.accounts:
            numm = self.accounts[ask]
            print(f"Account number : {numm.account_number}, Name : {numm.name}, Balance: {numm.balance}")
        elif ask not in self.accounts:
            raise ValueError ('Such account does not exist.')

    def deposit(self):
        ask = int(input("Enter the account number: "))
        if ask in self.accounts:
            numm = self.accounts[ask]
            deposit = int(input("Enter deposit amount: "))
            if deposit <= 0 or isinstance(deposit, str):
                print("Invalid deposit input! Try again")
            else:
                numm.balance += deposit
                print(f"The amount of ${deposit} has been successfully deposited. Current balance : ${numm.balance}")
        else:
            raise ValueError ("No such Account")
        self.save_to_file()
    def withdraw(self):
        ask = int(input("Enter the account number: "))
        if ask in self.accounts:
            numm = self.accounts[ask]
            withdraw = int(input("Enter the amount you want to withdraw: "))
            if withdraw <=0 or withdraw > numm.balance:
                print("Invalid withdraw input! Try again")
            else:
                numm.balance -= withdraw
                print(f"The amount of ${withdraw} has been withdrawn from the balance. Current balance: ${numm.balance}")
        else:
            raise ValueError ('No such account!')
        self.save_to_file()

    def save_to_file(self):
        data = {
            acc_num : acc.to_dict() for acc_num, acc in self.accounts.items()
        }
        with open("accounts.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        try:
            with open("accounts.json", "r") as f:
                data = json.load(f)
                for acc_num, acc_data in data.items():
                    int_acc_num = int(acc_num)
                    self.accounts[int_acc_num] = Account(
                        name=acc_data["Name"],
                        account_number=int_acc_num,
                        balance=int(acc_data["Balance"]),
                    )
        except FileNotFoundError:
            pass




John = Bank()
John.create_account('first', 100)
John.create_account('second', 500)
John.view_details()
John.deposit()
John.withdraw()
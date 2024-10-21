class Pet:
    #construtor
    def __init__(self, name, age, price="none"):
        self.name = name
        self.age = age
        self.__price = price

    #method
    def description(self):
        return f"Name: {self.name}, Age: {self.age}"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    def sleep(self):
        print("sleeping")

    #setter
    def set_price(self, p):
        self.price = p

    #getter
    def get_price(self):
        return self.price

class Dog(Pet):
    Legs = 4
    def __init__(self, species, name, age):
        self.species = species
        super().__init__(name, age)
    def bark(self):
        print("woof woof")
    def sniff(self, something):
        if something == "food":
            print(f"{something} smells good")
        else:
            print(f"{something} smells bad")

class Cat(Pet):
    legs = 4
    def __init__(self, breed, name, age):
        self.breed = breed
        super().__init__(name, age)

    def meow(self):
        print("meow")

    def sleep(self):
        print("sleeping 1")


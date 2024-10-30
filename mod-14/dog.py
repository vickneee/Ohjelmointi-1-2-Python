from animal import Animal


class Dog(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food

    def bark(self):
        print(f"{self.name} says Woof and eat {self.food}!")

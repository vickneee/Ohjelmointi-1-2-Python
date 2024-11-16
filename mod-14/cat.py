from animal import Animal


class Cat(Animal):
    def __init__(self, name, age, description):
        super().__init__(name, age)
        self.description = description

    def walking(self):
        print(f"{self.name} is walking outside!")

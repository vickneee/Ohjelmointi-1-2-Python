class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

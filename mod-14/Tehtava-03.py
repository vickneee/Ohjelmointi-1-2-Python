class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def plot(self):
        print(f"-- My name is {self.firstname} {self.lastname}")


class Student(Person):
    def __init__(self, firstname, lastname, student_nr):
        super().__init__(firstname, lastname)
        self.student_nr = student_nr

    def plot(self):
        super().plot()
        print(f"and my student number is {self.student_nr}")


p1 = Person("James", "Bond")
s1 = Student("Johnny", "English", 321)
p1.plot()
s1.plot()

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof Woof!")

jermanchapat = Dog("Tommy", "Jerman")
jermanchapat.bark()

class Person:
    def __init__(self, name):
        self.name = name
    
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print(f"Teacher Name: {self.name}")
        print(f"Subject: {self.subject}")

teacher_1 = Teacher("Sir Aneeq", "SDK")
teacher_1.display()
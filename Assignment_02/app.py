class Counter:
    object_count = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Counter.object_count += 1
    
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")
    
    @classmethod
    def get_object_count(cls):
        print(f"Total Students Created: {cls.object_count}")
    
student_1 = Counter("Mesum", 250)
student_2 = Counter("Ali", 300)
student_3 = Counter("Sara", 280)

Counter.get_object_count()

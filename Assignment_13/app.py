class Engine:
    def start_engine(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
    
car_1 = Car()
car_1.engine.start_engine()
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < 0:
            raise StopIteration
        else:
            val = self.start
            self.start -=1
            return val
        
for num in Countdown(5):
    print(num)
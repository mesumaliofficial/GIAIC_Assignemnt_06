class Multiplayer:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return 10 * self.factor

mul = Multiplayer(5)
print(mul(10))
class Logger:
    def __init__(self):
        print("Created")

    def __del__(self):
        print("Destroyed")

logger = Logger()   
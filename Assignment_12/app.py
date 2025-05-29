class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
check = TemperatureConverter()

print(check.celsius_to_fahrenheit(25))
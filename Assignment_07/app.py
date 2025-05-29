class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
    
    def get_ssn(self):
        return self.__ssn

ceo = Employee("Mesum", 500000, "42201-xxxxxxx-3")

print(ceo.name)       
print(ceo._salary)    
print(ceo.get_ssn())

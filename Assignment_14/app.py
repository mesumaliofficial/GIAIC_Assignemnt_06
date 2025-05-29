class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Department:
    def __init__(self, employe):
        self.employee = employe
    
emp_1 = Employee("Mesum", "102")
dept_1 = Department(emp_1)

print(f"Employee Name: {dept_1.employee.name}")
print(f"Employee Id: {dept_1.employee.id}")

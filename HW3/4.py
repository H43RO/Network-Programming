class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)


class Employee(Person):
    def __init__(self, name=None, age=0, employee_id=None):
        super().__init__(name, age)
        self.employee_id = employee_id

    def getEmployeeId(self):
        print(self.employee_id)


employee = Employee("IoT", 65, 2018)
employee.getName()
employee.getAge()
employee.getEmployeeId()

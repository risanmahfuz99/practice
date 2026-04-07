class Employee:
    companyName = "Divine IT"
    _count=0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee._count += 1

    # Instance Method
    def getInfo(self):
        return (f"Employee name: {self.name} with salary: {self.salary} in {self.companyName}")

    #classmethod
    @classmethod
    def countEmployees(cls):
        return cls._count

    # Static method — utility, no self or cls
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0

e1= Employee("Risan" , 0)
print(e1.getInfo())
e2 = Employee("Mahfuz" , 1)
print(e2.getInfo())
print(Employee.countEmployees())
print(Employee.is_valid_salary(e2.salary))

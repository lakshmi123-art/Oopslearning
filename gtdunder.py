class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
    def __gt__(self, other):
        return self.salary > other.salary
    def __lt__(self,other):
        return self.salary < other.salary
e1 = Employee("lakshmi",50000)
e2 = Employee("inchuu",35000)
print(e1 > e2)
print(e2 > e1)
print(e1 < e2)
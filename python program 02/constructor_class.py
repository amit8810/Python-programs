class Employee:
    
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        
    def getDetail(self):
        print(f"the name of employee is{self.name}")
        print(f"the age of the employee is {self.age}")
        print(f"the salary of the employee is {self.salary}")
        
amit=Employee("AMIT", 18, 1000)
amit.getDetail()







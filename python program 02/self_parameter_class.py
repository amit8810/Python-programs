class Employee:
    company="Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

        
amit=Employee()
amit.salary=100000
amit.getSalary()
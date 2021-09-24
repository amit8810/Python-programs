

class calculator:
    
    def __init__(self,num):
        self.number=num
        
    def square(self):
        print(f"The square of {self.number} is {self.number**2}")
    
    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")
    
    def squareroot(self):
        print(f"The SquareRoot of {self.number} is {self.number**0.5}")
    
a=calculator(9)
a.square()
a.cube()
a.squareroot()

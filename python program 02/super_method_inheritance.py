class person:
    
    def number(self):
        print("1234")
        
class employee(person):
    
    def number(self):
        super().number()
        print(123456)
        

        
p=person()
e=employee()



e.number()
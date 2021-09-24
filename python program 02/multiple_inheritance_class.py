#multiple heritance

class employee:
    company="google"
    
class education:
    company="sunderdeep"
    
class Amit(employee,education):
    
    def detail(self):
        print("owner name is amit")
        
a=Amit()
a.detail()
print(a.company)
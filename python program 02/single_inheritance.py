
#single inheritance


class employee():
    company="Google"
    def detail(self):
        print("this is an employee")
class programmer(employee):
    language="Python"
    
    def getinfo(self):
        print("this is a coder")
        
    def detail(self):
        print("working in Google")    #overwite
e=employee()
#e.detail()
p=programmer()
p.detail()
print(p.company)
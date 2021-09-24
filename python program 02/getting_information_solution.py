class programmer:
    company="Microsoft"
    
    def __init__(self,name,product):
        self.name=name
        self.product=product
        
    def getDetail(self):
        print(f"name={self.name}")
        print(f"product={self.product}")
        print(f"company = {self.company}")
        
amit=programmer("amit","GitHub")
arslaan=programmer("arslaan","Twitter")

amit.getDetail()

print("\n")


arslaan.getDetail()

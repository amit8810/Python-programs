class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
v1=Vector(1, 4, 6)
v2=Vector(1, 6, 9)
print(v1)
print(v2)
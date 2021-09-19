def Nsum(n):
    if n==1 or n==0:
        return 1
    else:
        return n+Nsum(n-1)
s=Nsum(5)
print(s)
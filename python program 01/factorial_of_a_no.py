num=int(input("enter the no : "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
#print("the factorial of the number is ", str(factorial))
print(f"The factorial of {num} is {factorial}")
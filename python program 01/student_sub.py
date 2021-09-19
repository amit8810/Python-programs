sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail")
if((sub1+sub2+sub3)/3 <40):
    print("you are fail")
else:
    print("you are pass")
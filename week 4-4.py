a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("enter the value of c:"))
if(a>b and a>c):
    maximum=a
    minimum=b if b<c else c
elif(b>a and b>c):
    maximum=b
    minimum=a if a<c else c
else:
    maximum=c
    minimum=b if b<a else a
print("Maximum number is:",maximum)
print("Minimum number is:",minimum)

n=int(input("Enter the value of n:"))
a,b=0,1
print("Fibonacci series upto",n,"is:")
for i in range(1,n+1):
    print(a,end=" ")
    a,b=b,a+b


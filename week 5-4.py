n=int(input("Enter the value of n:"))
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print("Fibonacci series upto",n,"numbers is:")
for i in range(n):
    print(fib(i),end=" ")

n=int(input("Enter the value of n:"))
def prime(n, i=2):
    if n <= 1:
        return 0
    if i == n:
        return 1
    if n % i == 0:
        return 0
    return prime(n, i + 1)
if prime(n):
    print("Prime number")
else:
    print("Not a prime number")

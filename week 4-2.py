n=int(input("Enter the value of n:"))
even_count=0
odd_count=0
for i in range(n):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("No.of even numbers:",even_count)
print("No.of odd numbers:",odd_count)

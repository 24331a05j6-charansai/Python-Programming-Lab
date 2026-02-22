n = int(input("Enter number of tuples: "))
TupleList = []
for i in range(n):
    n1= int(input("Enter first element: "))
    n2 = int(input("Enter second element: "))
    TupleList.append((n1,n2))
TupleList.sort(key=lambda x: x[-1])
print("Sorted list:", TupleList)

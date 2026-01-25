def displayList(lst):
    print("Elements in the list are:")
    for i in lst:
        print(i, end=" ")
n = int(input("Enter number of elements: "))
myList = list(map(int, input("Enter elements: ").split()))
displayList(myList)

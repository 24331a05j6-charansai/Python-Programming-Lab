dct={"Names":["charan","sai"],"Marks":[10,45]}
print(dct)
print("Keys are:",dct.keys())
print("Values are:",dct.values())
print("Items are: ",dct.items())
dct.pop("Names")
print("After pop Dictionary is:",dct)
del dct["Marks"]
print("After Delete Dictionary is:",dct)

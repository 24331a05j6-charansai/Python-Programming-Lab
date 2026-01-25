s=input("Enter a string:")
rev=s[::-1]
print(rev)
if rev==s:
    print("The given string",s,"is palindrome")
else:
    print("The given string",s,"is not a palindrome")

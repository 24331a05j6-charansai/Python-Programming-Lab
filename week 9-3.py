import random
file=open("Random number generation.txt","w+")
num=int(input("Enter the value of n:"))
for i in range(num):
    n = random.randint(1, 100)
    file.write(str(n) + "\n")
contents=file.read()
print(contents)
file.close()
print("20 Random numbers from 1 to 100 written to Random number generation.txt ")

p=int(input("Enter the principle amount:"))
r=int(input("Enter the rate of interest:"))
t=int(input("Enter time:"))
n=int(input("Enter The no.of time the interest is increased per year:"))
amount=p*(1+r/n)**(n*t)
print(amount)
ci=amount-p
print(ci)

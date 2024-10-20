#  Python Program to Find HCF or GCD 

n1=int(input("Enter first num:"))
n2=int(input("Enter second num:"))
if n1<n2:
    small=n1
else:
    small=n2
for i in range(1,small+1):
    if (n1%i==0) & (n2%i==0):
        hcf=i
print(hcf)


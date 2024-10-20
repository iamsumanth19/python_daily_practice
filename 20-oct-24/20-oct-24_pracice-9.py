#  Python Program to Check Armstrong Number 
n=int(input("Enter a number:"))
s=str(n)
l=len(s)
sum=0
for i in range (0,l):
        sum=sum+(int(s[i]))**l
if sum==n:
    print("It's a amstrong number!!")
else:
    print("It's not a amstrong number!!")

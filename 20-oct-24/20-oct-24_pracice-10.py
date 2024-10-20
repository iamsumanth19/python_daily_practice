#  Python Program to Find the Sum of Natural Numbers 
n = int(input("Enter no,of first natural numbers:"))
sum=0
for i in range(0,n+1):
    sum+=i
print(f"The sum of first {n} natural numbers is {sum}.")
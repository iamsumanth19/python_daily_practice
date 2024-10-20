#  Python Program to Find the Factorial of a Number 
num=int(input("Enter a number:"))
count=1
for i in range(num,1,-1):
    count*=i
print(f"The factorial of {num} is {count}")


#  Python Program to Print the Fibonacci sequence
n=int(input("Enter the no.of terms:"))
a=0
b=1
series=[0,1]
for i in range(n):
    c=a+b
    series.append(c)
    a=b
    b=c
print(f"fibinacii series is {series}")

# Python Program to Solve Quadratic Equation 
a=int(input("enter the 'a' value in quadratic equation:"))
b=int(input("enter the 'b' value in quadratic equation:"))
c=int(input("enter the 'c' value in quadratic equation:"))
d=b*b-4*a*c
e=d**0.5
root_1=(-b+e)/2*a
root_2=(-b-e)/2*a
print(f"Roots are {root_1,root_2}")
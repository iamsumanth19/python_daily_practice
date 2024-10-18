# Swap two variables without using a temporary variable.

a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
a=a+b
b=a-b
a=a-b

print(f"the two numbers are {a},{b}")


 # Create a simple calculator (addition, subtraction, multiplication, division).

a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
operation=input("Enter thr operation in (+,-,*,/) only:")
addition= a+b 
subraction=a-b
multiplication=a*b
division=a/b
if operation == '+':
    print(addition)
elif operation=='_':
    print(subraction)
elif operation=="*":
    print(multiplication)
elif operation=="/":
    print(division)
else:
    print("Operator is out of bound!!")

    
   

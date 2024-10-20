# Let's convert the decimal number 13 to binary.
# 13 ÷ 2 = 6 remainder 1
# 6 ÷ 2 = 3 remainder 0
# 3 ÷ 2 = 1 remainder 1
# 1 ÷ 2 = 0 remainder 1
n=int(input("Enter a number:"))
s=""
while n>0:
    r=n%2
    s+=str(r)
    n=n//2
binary=s[::-1]
print(f"The binary value of {n} is {binary}")



# Write a Python Program to Check Leap Year.
year=int(input("Enter the year:"))
if year%400==0 & year%100==0:
    print(f"{year} is a leap year!!")
elif  year%4==0 & year%100!=0:
     print(f"{year} is a leap year!!")
else:
      print(f"{year} is not a leap year!!")
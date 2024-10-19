 # Check if two strings are anagrams.
str_1=input("Enter first String:")
str_2=input("Enter second String:")
a=str_1.upper()
b=str_2.upper()
if sorted(a)==sorted(b):
    print('given two words are anagrams!!')
else:
    print('given two words are not anagrams!!')



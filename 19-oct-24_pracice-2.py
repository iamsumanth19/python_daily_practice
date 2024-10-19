 #  Check if a string is a palindrome

word=input("enter the word:")
r_word=word[len(word)::-1]
if word==r_word:
    print("Given word is a palindrome!!")
else:
    print("Given word is not a palindrome!!")
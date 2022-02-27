# 58.	Write a Python function that checks whether a passed string is palindrome or not.

string= input("Enter a string: ")
if string== string[::-1]:
    print("The passed string is palindrome")
else:
    print("It is not a palindrome")
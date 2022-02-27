#41.	Write a Python program to reverse a string.

string= input("Enter a string: ")
print("The reversed string is",string[::-1])
    
# using recursion
def reverse_str(str):
    if str==1:
        return str
    else:
        return reverse_str(str[1:])+ str[0]
str= input("enter a string: ")
str1= reverse_str(str)
print("The reversed string is: ",str1)
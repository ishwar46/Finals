# 60.	Write a Python program to reverse a string using recursion
def reverse_str(str):
    if len(str)==1:
        return str
    else:
        return reverse_str(str[1:]) + str[0]

str= input("enter a string: ")
rev= reverse_str(str)
print(rev)
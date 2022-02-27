# 43.	Write a program function to find max of three numbers.

one= int(input("Enter the first number: "))
two= int(input("Enter the second number: "))
three= int(input("Enter the third number: "))
if one>two and one>three:
    print("The max number is", one)
elif two>one and two>three:
    print("The max number is", two)
else:
    print("The max number is", three)
#Faulty Calculator
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

print("Enter first number:")
x=int(input())
print("Enter second number:")
y=int(input())
print("Which operation you want to perform?")
s=input()
if s==("+") and x==56 and y==9:
    print("Your answer is",77,".")
elif s==("+") and x==9 and y==56:
    print("Your answer is",77,".")
elif s==("*") and x==45 and y==3:
    print("Your answer is",555,".")
elif s==("*") and x==3 and y==45:
    print("Your answer is",555,".")
elif s==("/") and x==56 and y==6:
    print("Your answer is",4,".")
elif s==("/") and x==6 and y==56:
    print("Your answer is",(4),".")
elif s==("+"):
    print("Your answer is",x+y,".")
elif s==("*"):
    print("Your answer is",x*y,".")
elif s==("/"):
    print("Your answer is",x/y,".")
else:
    print("Please try again")
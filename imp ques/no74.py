# 74.	Given three integers, print the smallest one. (Three integers should be user input)

num1 = int(input("ENter"))
num2 = int(input("Enter"))
num3 = int(input("ENter"))

if num1<num2 and num1<num3:
    print(num1,"smallest")
elif num2<num1 and num2<num3:
    print(num2,"Smallest")
else:
    print(num3,"smallest")
"""
write a program to check whether a person is eligible for voting or not.(Accept age from user)
"""
age= int(input("Enter your age: "))
if age>=18:
    print("You are eligible for voting")
else:
    print("Your are not eligible for voting")
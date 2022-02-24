#if else and elif
print("Welcome to DOTM Nepal")
age = int(input("Enter your age"))
if age > 18:
    print("You are eligible to drive")
elif age == 18:
    print("Please visit our office")
elif age < 18:
    print("You are not eligible to drive")
else:
    print("Invalid Input")
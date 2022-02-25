#Write a program to accept percentage from the user and display the grade according to the following criteria:

print("Welcome to exam office")

math = int(input("Enter"))
programming = int(input("Enter"))
database = int(input("Enter"))
android = int(input("Enter"))
sd = int(input("Enter"))

avg = (math+programming+database+android+sd)/5

if avg >= 90:
    print("Grade A")
elif avg > 80 and avg <= 90:
    print("Grade B")
elif avg >= 60 and avg <= 80:
    print("Grade C")
else:
    print("Grade D")

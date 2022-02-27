'''
38.	Write a program to accept a number from 1 to 12 and display name of the month like 1 for January, 2 for February and so on.
'''
print("Date Finder")


def month(x):
    if (x == 1):
        print("Jan")
    if (x == 2):
        print("Feb")
    if (x == 3):
        print("March")
    if (x == 4):
        print("April")
    if (x == 5):
        print("May")
    if (x == 6):
        print("June")
    if (x == 7):
        print("July")
    if (x == 8):
        print("August")
    if (x == 9):
        print("September")
    if (x == 10):
        print("October")
    if (x == 11):
        print("November")
    if (x == 12):
        print("December")
    if (x < 1 or x > 12):
        print("Invalid input")

months = int(input("Enter the month number: "))
month(months)



def days (a):
    if a == 1:
        print("Sunday")
    if a == 2:
        print("Mon")
    if a == 3:
        print("Tue")
    if a == 4:
        print("Wed")
    if a == 5:
        print("Thu")
    if a == 6:
        print("Fri")
    if a == 7:
        print("Sat")
    if a<1 or a>7:
        print("Invalid Input")
num = int(input("Enter the number from 1 to 7: "))
days(num)








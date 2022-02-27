'''
38.	Write a program to accept a number from 1 to 12 and display name of the month like
 1 for January, 2 for February and so on.
'''

number= int(input("Enter a number: "))
if number==1:
    print("1 for January")
elif number==2:
    print("2 for February")
elif number==3:
    print("3 for march")
elif number==4:
    print("4 for April")
elif number==5:
    print("5 for May")
elif number==6:
    print("6 for June")
elif number==7:
    print("7 for July")
elif number==8:
    print("8 for August")
elif number==9:
    print("9 for September")
elif number==10:
    print("10 for October")
elif number==11:
    print("11 for November")
elif number==12:
    print("12 for December")
else:
    print("Enter a number between 1 to 12")
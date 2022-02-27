"""
Write a program to accept a number from 1 to 7 and display the name of the day like
1 for sunday, 2 for Monday and so on
"""

num= int(input("Enter a number: "))
if num==1:
        print(f"{num} for Sunday")
elif num==2:
        print(f"{num} for Monday")
elif num==3:
        print(f"{num} for Tuesday")
elif num==4:
        print(f"{num} for Wednesday")
elif num==5:
        print(f"{num} for Thursday")
elif num==6:
        print(f"{num} for Friday")
elif num==7:
        print(f"{num} for Saturday")
else:
    print("error")
    

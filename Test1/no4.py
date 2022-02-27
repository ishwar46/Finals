"""
write a program to accept a percentage 
from the user and display the grade according to the following criteria

Marks               Grade
>90                  A
>80 & <=90           B
>=60 & <=80          C
below 60             D

"""

percentage= int(input("Enter your percentage: "))
if percentage>90:
    print("Grade A")
elif percentage>80 and percentage<=90:
    print("Grade B")
elif percentage>=60 and percentage<=80:
    print("Grade C")
else:
    print("Grade D")
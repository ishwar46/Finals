'''''
29.	A school decided to replace the desks in three classrooms. 
Each desk sits three students. Given the number of students in each class, 
print the smallest possible number of desks that can be purchased. 
The program should read three integers: the number of students in each of the three 
classes, a, b and c respectively.

'''
a= int(input("Enter the number of student in class a: "))
b= int(input("Enter the number of student in class b: "))
c= int(input("Enter the number of student in class c: "))
if a%3==0:
    no_of_desk_in_a= a//3
else:
    no_of_desk_in_a= (a//3)+1

if a%3==0:
    no_of_desk_in_b= b//3
else:
    no_of_desk_in_b= (b//3)+1

if a%3==0:
    no_of_desk_in_c= c//3
else:
    no_of_desk_in_c= (c//3)+1

print(f"The smallest number of desks that can be purchased are { no_of_desk_in_a+no_of_desk_in_a+no_of_desk_in_a}")


'''
36.	A school decided to replace the desks in three classrooms. 
Each desk sits three students. Given the number of students in each class,
print the smallest possible number of desks that can be purchased. 
The program should read three integers: the number of students in each of the three 
classes, a, b and c respectively.
'''
A= int(input("Enter the number of students in class A: "))
B= int(input("Enter the number of students in class B: "))
C= int(input("Enter the number of students in class C: "))
if A%3==0:
    students_in_class_A= A//3
else:
    students_in_class_A= (A//3)+1
if B%3==0:
    students_in_class_B= B//3
else:
    students_in_class_B= (B//3)+1
if C%3==0:
    students_in_class_C= C//3
else:
    students_in_class_C= (C//3)+1
print(f"The number of desks needed to be purchased are{students_in_class_A+students_in_class_A+students_in_class_A}")



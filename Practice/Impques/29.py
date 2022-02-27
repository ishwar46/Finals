'''
29.	A school decided to replace the desks in three classrooms. Each desk sits three students.
Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three
classes, a, b and c respectively.
'''

a = int(input("Enter: "))
b = int(input("Enter: "))
c = int(input("Enter: "))

print(a//2+b//2+c//2+a%2+b%2+c%2)

stringg = input("Enter a string")

print(stringg[::-1])




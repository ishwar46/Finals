#Result
'''sub1=float(input("Enter marks of the first subject: "))
sub2=float(input("Enter marks of the second subject: "))
sub3=float(input("Enter marks of the third subject: "))
sub4=float(input("Enter marks of the fourth subject: "))
sub5=float(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")
    '''

a = float(input("Enter Marks in English :\t"))
b = float(input("Enter Marks in Maths: \t"))
c = float(input("Enter Marks in Physics: \t"))
d = float(input("Enter Marks in Chemistry: \t"))
e = float(input("Enter Marks in Computer Science: \t"))
avg = ((a + b + c + d + e) / 500) * 100
if (avg >= 90):
    print("Congratulations ! You have secured Grade A, and your percentage is ", avg)
elif (avg >= 70 and avg < 80):
    print("Congratulations ! You have secured Grade B and your percentage is ", avg)
elif (avg >= 60 and avg < 70):
    print("Congratulations ! You have secured Grade C, and your percentage is ", avg)
elif(avg>= 50 and avg < 60):
    print("Congratulations ! You have secured Grade D, and your percentage is ", avg)
else:
    print("You are fail")

n = 5
for i in range(n):
    print('*' * (i+1))
for j in range(n):
        print('*' * (n-j-1))
print()

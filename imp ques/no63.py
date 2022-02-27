# 63.	Write a Python program to get the Fibonacci series between 0 to 50

n=50
x=0
y=1
z=0
while (z<=n):
    x=y
    y=z
    z= x+y
    print(z)
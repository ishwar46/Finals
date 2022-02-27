# 96.	Write a program to find the product of the digits of a number accepted from the user. 

num= int(input("Enter a number: "))
product=1
while num>0:
    digit= num%10
    product=product*digit
    num= num//10
print("The product is: ",product)

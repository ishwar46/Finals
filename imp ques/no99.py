# 99.	Write a program to accept 10 numbers from the user 
#  and display the largest and smallest number.
list=[]
for i in range(10):
    A= int(input("Enter a number: "))
    list.insert(1,A)
print("the largest number is: ", max(list))
print("The smallest number is: ", min(list))

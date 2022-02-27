# 66.	Write a Python program to print a specified list after removing the 0th, 4th and 5th elements

list1 = ["Hello","How","Are",1,2,3,4,"You"]
print("This is the orignal list\n", list1)
del list1[0]
del list1[4]
del list1[5]

print("Remaing items in the list",list1)
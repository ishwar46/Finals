# 46.	Write a Python program to find the 2nd largest number in a list.

list= [4,5,6,7,8,2,3]
list.sort() # sorting the given list so that we can find through indexing
print("The second largest number is", list[-2])
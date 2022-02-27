# 102.	Write a program to print only odd numbers from the given list using while loop.
# L=[23,45,32,25,46,33,71,90,45,88]

'''list=[23,45,32,25,46,33,71,90,45,88]
i= 0
while (i<len(list)):
    if i%2!=0:
        print(list[i],end=",")
    i=i+1'''

# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

only_odd = [num for num in list1 if num % 2 == 1]

print(only_odd)



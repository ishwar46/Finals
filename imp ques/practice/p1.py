#To print simple for many times

#  for i in range(0,5):
#     print(f"Hello Wrold {i}")
#     print(f"Learning{i}")



# cam= "Camera"
# for i in cam:
#     print(i, end="") 


# using range 

# cam= range(5,15)
# for i in cam:
#     print(i)

#using length and all
# 0 = P
# 1 = R

# st= "Programming"
# n= len(st)   This is quite important cocept
# for i in range(n):
#     print(i,"=",st[i])


# Else part # this will print the else part only once and at the end

# st= "Programming"
# for i in st:
#     print("Okay")
# else:
#     print("Not okay")


# ask user to input username and password and enter username and 
# password for 3 times and thrwo invalid credential if wrong and 
# throw attempt finished after wrong attempt 3 times


# username= int(input("Enter a username: "))
# password= int(input("Enter your password: "))
# print("Enter your credentials")
# for i in range(0,3):
#     username1= int(input("Enter your username: "))
#     password1= int(input("Enter your password: "))
#     if username==username1 and password==password1:
#         print("Logged in successfully")
#         break
#     else:
#         if username!=username1 and password!=password1:
#             print("Invalid Credential")
        
# else:
#         print("Attempt finished")


# if you want to fix answer
# for i in range(0,3):
#     a= input("Enter a number: ")
#     if int(a)==123:
#         print(True)
#         break
#     else:
#         print(False)

# nested for loop
# for i in range(2):
#     print("*",i)
#     for j in range(3):
#         print("#",j)

# for i in range(6):
#     print("")
#     for j in range(i):
#         print("*", end="")

# for i in range(5):
#     print("")
#     for j in range(i+1):
#         print("*", end="")

# for i in range(5):
#     print("",i)
#     for j in range(i+1):
#         print("*", end="")
# for i in range(5):
#     print("*") # made nepal ko jhanda


# for i in range(4):
#     print("")
#     for j in range(10):
#         print("*",end= "")

# for i in range(10):
#     print("",i)
#     if i<=5:
#         for j in range(i):
#             print("*", end="")
#     else:
#         for j in range(10-i):
#             print("*", end="")

# break statement

# for i in range(10):
#     if i==5:
#         continue
#     print(i)
# print("sdfv")

# python program to add all the item of list
# 2 methods tala wala more accurate
# list= [11,5,17,18,23]
# total=0
# for i in list:
#     total= total+i
#     print(total)

# list= [11,5,17,18,23]
# total=0
# for i in range(0, len(list)):
#     total= total+list[i]
# print("Sum of all elements of the list is:",total)


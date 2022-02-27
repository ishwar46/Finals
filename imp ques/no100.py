# 100.	Write a program to display all the numbers which are divisible by 13 
# but not by 3 between 100 and 500.

for i in range(100,500):
    if i%13==0 and i%3!=0:
        print(i)
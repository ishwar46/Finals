# 71.	Write a Python script to generate and print a dictionary 
# that contains a number (between 1 and n) in the form (x, x*x). 
# Sample Dictionary ( n = 5) : Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


dict={}
num= int(input("Enter the number up to which you wanna generate: "))
for i in range(1,num+1):
    dict[i]=i**2
print(dict)

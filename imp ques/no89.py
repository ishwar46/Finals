# Write a program that prompts the user to input a positive integer.
#  It should then print the multiplication table of that number. 

def multiplication(num,i):
    # basecase
    if (i>10):
        return 1
    print(num,"*",i,"=", num*i)
    # calling the function
    return multiplication(num, i+1)

num= int(input("Enter a number you want a multiplication table of: "))
multiplication(num,1)


num = int(input("Enter the number of table you want: "))

for i in range(1,11):
    print(num,"x",i,'=',num*i)
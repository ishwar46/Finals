'''
42.	Accept string from the user and display only those characters which are 
present at an even index.
'''

# string= input("Enter a string: ")
# print("The characters present at an even index are", string[::2])

# using for loop

string= input("Enter a string: ")
for i in string[::2]:
    print(i, end="")

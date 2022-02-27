"""
write a python script to print a dictionary where the keys are numbers between 1 and 15
(both included)and the values are square of keys.
sample Dictionary
{1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100,11:121,12:144,13:169,14:196,15:225}
"""

# Factorial of a number using recursion

def ref_fac(x):
    if x == 1:
        return x
    else:
        return x*ref_fac(x-1)
number = 5

if number<0:
    print("No factorial for negative number")
elif number == 0:
    print("Fac of O is 1")
else:
    print("The fac of",number,"is",ref_fac(number))
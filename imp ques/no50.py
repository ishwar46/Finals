# 50.	Write a Python program to convert a tuple to a string.

def convertTuple(tuple):
        # initialize an empty string
    str = ''
    for i in tuple:
        str = str + i
    return str

# Driver code
tuple = ('h', 'e', 'l', 'l', 'o')
str = convertTuple(tuple)
print(str)


# 49.	Write a Python program to add an item in a tuple.

tuple= (1,2,3,4,5,6)
#As we know tuples are immutable data structures and we can not directly add items to it, so by creating a 
# variable or directly adding value using ‘+’ operator will do the work of adding the single item in tuple
var= 7
tuple += (var,) # we used , because tuple accpets , otherwise its a different datatype
print(tuple)

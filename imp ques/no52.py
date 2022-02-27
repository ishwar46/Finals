# 52.	Write a Python program to sum all the items in a dictionary.


# Function to print sum
def returnSum(myDict): 
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
     
    return final
 
# Driver Function
myDict = {'a': 100, 'b':200, 'c':300}
print("Sum :", returnSum(myDict)) # value same aaucha paramemter same 
                                  #rakhey pani aarko raakey pani




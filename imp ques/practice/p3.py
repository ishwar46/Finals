# list
# list are ordered mutable and accepting duplicate
# [1,2,3,4]

#slicing and indexing
# list=[1,2,3,4,5]
# print(list[2])
# print(list[0:5])

# using range
# list= list(range(0,10,1))
# print(list)
list= ["Roshan","Harry",3,4]
list.append(9)
list.insert(1,"Hello")
tuple= (1,2)
list.insert(3,tuple)
list[2]=2
print(list)
del list[0]
list.remove("Hello")
list.pop()
list1= ["a","b"]
list0= list+list1

print(list0)



numbers = ["1", "2", "4", "22"]
numbers.append(4)
print(numbers)

list1 = ["11", "22", "33", "44", "20"]
#list1.sort()
list1.reverse()
print(list1)
print(list1[2])

list1 = ["33", "21", "2", "1", "42"]
print(list1[:4])
print(list1[1:])
print(list1[1:4])

#extend slicing
#append
school = ["Principle", "Teachers", "Staffs", "Students"]
school.append("Name")
print(school)

#insert
friends = ["Sam", "Rox", "Dhawit"]
friends.insert(1,"Sneha")
print(friends)

#remove
grocery = ["Shampoo", "Soap", "Toothbrush", "Deo"]
grocery.remove("Soap")
print(grocery)

#pop
highway = ["E-W","BP","Prihivi","Arniko"]
highway.pop()
print(highway)

#Access and change elemnets
roads = ["bhaktapur","kathmandu","lalitpur","butwal"]
roads[3]= "Rajbiraj"
print(roads)
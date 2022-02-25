#for loop

'''list1 = ["Ishu", "Sam", "Roz", "Dhawit", "Sneha"]
for i in list1:
    print(i)'''

list1 = [["Ishu", 20,],
         ["Sam", 20,],
         ["Roz", 22,],
         ["Dhawit", 19,],
         ["Sneha", 19]]
for item, age in list1:
    print(item, "is", age,"years old")

#type casting
hello = [["Ishu", 20,],
         ["Sam", 20,],
         ["Roz", 22,],
         ["Dhawit", 19,],
         ["Sneha", 19]]
dict1 = dict(hello)
for itemnew in dict1:
    print(itemnew)

#while loop

i = 0
while(i<20):
    print(i)
    i = i+1

#break and continue

i = 0
while(True):
    if i + 1 <5:
        i= i+1
        continue
    print(i+1, end=" ")
    if(i==44):
        break
    i = i+1

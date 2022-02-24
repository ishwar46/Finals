"""
“Python dictionary is an unordered collection of items.
Each item of the dictionary has a key and value pair/ key-value pair.”
"""

dict = {"Ishu":"Pizza",
        "Roz":"Burger",
        "Sneha":"Rolls"}
print(dict)

dictadd = {"Ishu":"Ktm",
           "Roz":"Ktm",
           "Dhawit":"Chitwan",
           "Sneha":{"Temp":"Kathmandu","Perma":"Lalitpur"}}
print(dictadd)
dictadd["Sam"] = "Cape"
dictadd["Sadikshya"] = "Lalitpur"
dictadd[123] = "Address"
print(dictadd)
del dictadd[123]
print(dictadd)

dictnew = dictadd.copy()
del dictnew["Roz"]
print(dictnew)


print(dict.get("Ishu"))

dictadd.update({"Prajina":"Junkfood"})
print(dictadd)

print(dictadd.keys())
print(dictadd.values())
print(dictadd.items())

print("Welcome to my Dictonary")
dictonary = {"Apple":"Fruit",
             "Ball":"Toy",
             "Cat":"Animal"
             }
print(dictonary.keys())
print("The meaning of: ")
result = input()
##print("The meaning is",dictonary[result])
print(dictonary[result])
print("Thank you for using my dictonary")
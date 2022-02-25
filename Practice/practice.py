#Python Dictionary

print("Welcome to my Dictionary")
dictnew = {"Harshika": "Girl",
        "Dhawit": "Boy",
        "Sneha":"Girl",
        "Prabin":"Boy"
        }
print("Enter name to know gender: ")
result = input()
print("Entered person is a ",dictnew[result])

#for loop

list1 = [int,float,"ishu","roz",1,2,3,6,7,6,8,"shampoo",["lol",2],"hello"]

for i in list1:
        if str(i).isnumeric() and i >6:
                print(i)

#while and break and continue

while(True):
        i = int(input("Enter any number\n"))
        if i<100:
                print("Try again\n")
                continue
        else:
                print("Congratulations")
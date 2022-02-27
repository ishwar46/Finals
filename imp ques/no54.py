# 54.	N students take K apples and distribute them among each other evenly. 
# The remaining (the undivisible) part remains in the basket. 
# How many apples will each single student get?
#  How many apples will remain in the basket? 
# The program reads the numbers N and K.
#  It should print the two answers for the questions above.



'''N= int(input("Enter the number of students: "))
K= int(input("Enter the number of aplles: "))
each_single_student_gets= K//N
apples_remaining_in_the_basket= K%N
print(f"each student gets {each_single_student_gets} and apples remained in the basket are {apples_remaining_in_the_basket}")'''

n = int(input("ENter the number of students: "))
k = int(input("Enter the number of apples: "))

apple = (k//n)
remaining = (k%n)
print("Each student will get",apple,"apples")
print("remaing apple in the basket",remaining)



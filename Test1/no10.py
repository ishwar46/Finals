"""
write aprogram to check whether a number(accepted from user) is divisible by 2 and 3 both
"""
num= int(input("Enter a number: "))
if num%2==0 and num%3==0:
    print("The number is divisible by both 2 and 3")
else:
    print("The number is not divisible by both 2 and 3")
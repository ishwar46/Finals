#Python Dictionary

'''print("Welcome to my Dictionary")
dictnew = {"Harshika": "Girl",
        "Dhawit": "Boy",
        "Sneha":"Girl",
        "Prabin":"Boy"
        }
print("Enter name to know gender: ")
result = input()
print("Entered person is a ",dictnew[result])'''

#for loop

'''list1 = [int,float,"ishu","roz",1,2,3,6,7,6,8,"shampoo",["lol",2],"hello"]

for i in list1:
        if str(i).isnumeric() and i >6:
                print(i)'''

#while and break and continue

'''while(True):
        i = int(input("Enter any number\n"))
        if i<100:
                print("Try again\n")
                continue
        else:
                break
                print("Congratulations")'''

#guess the number

n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")


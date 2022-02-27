'''def fizzbuz(num):
    if (num%5==0 and num%3==0):
        print("buzz")
    elif num%3==0:
        print("buzz")
    elif num%5==0:
        print("fizz")
    else:
        print(num)
fizzbuz()'''


def Fizz_Buzz(x):
    for x in range(0, x):
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)
    int(input("Num"))
    Fizz_Buzz(x)
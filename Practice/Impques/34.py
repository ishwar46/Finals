'''34.	Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number.
'''
for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
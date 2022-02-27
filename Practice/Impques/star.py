print("Print equilateral triangle Pyramid using asterisk symbol ")
# printing full Triangle pyramid using stars
size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()

col = 5
row = 10
for i in range(5):
    for j in range(10):
        print("*", end=" ")
    print()

def stars(rows):
    for i in range(0,rows):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\t")
row = 5
stars(rows)

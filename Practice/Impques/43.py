#Accept string from the user and display only those characters which are
#present at an even index.

new_string = input('Enter a string: ')
even = []
for i in range(len(new_string)):
    if i % 2 == 0:
        even.append(new_string[i])
print('Even characters: {}'.format(even))
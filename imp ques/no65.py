# 65.	Write a Python program to count the number of strings where the string length is 2
# or more and the first and last character are same from a given list of strings. 
# Sample List: ['abc', 'xyz', 'aba', '1221']
# Expected Result: 2

list= ['abc', 'xyz', 'aba', '1221']
# for i in list:
#     if list[0]==list[-1]:
#     print(len(list))

for i in list:
    if len(i) >= 2 and i[0] == i[-1]:
        print(i)

'''def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))'''

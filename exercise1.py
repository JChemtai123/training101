sentence = "The dog finished the pie"
# write a python program to answer below questions
# 1. how many words are in the string
# 2. what is the length of string sentence
# 3. how many times does word "dog" appear
# 4. write a new string similar ro sentence except that all letters are capital

words= len(sentence)
print(words)

print(sentence.upper())

print(sentence.count("dog"))
words1 = str.split(sentence)
# print(words1)
print(len(words1))
to_list= sentence.split()
print(to_list)
tasklist= [23, "Jane",["Lesson 23",560,{"currency":"KES"}], 987,(76,"John")]
print(tasklist)

# 1. determine the type of variable tasklist using an inbuilt function
# 2. print Kes
# 3. print 560
# 4. use a function to determine the length of tasklist
# 5. change 987 to 789 using an inbuilt function
# 6. change name "John" to "Jane"
type_of_var= type(tasklist)
print(type_of_var)
#def my_function():
#print kes
print(tasklist[2][2]["currency"])
# print 560
print(tasklist[2][1])
# change 987 to 789, reversing a string use ::-1, change integer to string coz you cannot reverse an interger
print(str(tasklist[3])[::-1])
# or
tasklist.pop(3)
tasklist.insert(3,789)
print(tasklist)

# deleting a list
# del(list)

# change name John to Jane
# not possible




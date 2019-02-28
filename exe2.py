tasklist1= [23, "Jane",["Lesson 23",560,{"currency":"KES"}], 987,(76,"John")]
print(tasklist1)

# 1. determine the type of variable tasklist using an inbuilt function
# 2. print Kes
# 3. print 560
# 4. use a function to determine the length of tasklist
# 5. change 987 to 789 using an inbuilt function
# 6. change name "John" to "Jane"
type_of_var= type(tasklist1)
print(type_of_var)
#def my_function():
    #print("KES")
kes1 = tasklist1[2]
kes11= kes1[2]
print(kes11["currency"])

# print 560
num= kes1[1]
print(num)

# use fxn to find len of tasklist
print(len(tasklist1))

# change 987 to 789
rev= tasklist1[3]
print(rev)


#x = input("12345")

# Enter a number 12345

#Y = x[len(x)-1:0:-1]+x[0]

#print(Y)

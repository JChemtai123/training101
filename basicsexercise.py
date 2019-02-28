# 1. Write a program which accepts a string as input to print "Yes" if the string is "yes",
# "YES" or "Yes", otherwise print "No".
# Hint: Use input () to get the persons input
#string = input("enter a string")
# if string = "yes":
#        print("YES")
#  else:
#        print("NO")
y3= input("please enter a string:")
if y3=="YES" or y3=="Yes" or y3=="yes":
    print("yes")
else:
    print("no")


# 2.Implement a function that takes as input three variables, and returns the largest of the three.
# Do this without using the Python max () function!
# The goal of this exercise is to think about some internals that Python normally takes care of for us.

def max(X,Y,Z):
    if X> Y and X> Z:
        return(X)
    elif Y> X and Y> Z:
        return(Y)
    elif Z> X and Z> Y:
        return(Z)
    elif X==Y and X>Z:
        return(X)
    elif Y==Z and Y>X:
        return(Y)
    elif X==Z and Z>Y:
        return(Z)

    else:
        print("all numbers are equal")

print(max(100,100,95))
# 3.Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and
# last elements of the given list. For practice,write this code inside a function
def listofnumbers(ls):
    newlist= ls[0], ls[-1]
    return newlist

list1= (input("please enter a list "))
list1 = list1.split(",")
extractedlist= listofnumbers(list1)
print(extractedlist)


# 4. Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Hint: how does an even /
# odd number react differently when divided by 2? Extras:
# 1. If the number is a multiple of 4, print out a different message

Number = int(input("Enter a number"))
if Number % 2== 0:
    print("you have entered an even number")
elif Number % 2!= 0:
    print("You have entered an odd number")
else:
    print("null")



#5. With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
# write a program to print the first half values in one line and the last half values in one line.


    tuples= (1,2,3,4,5,6,7,10,23,21)
    tuple1 = tuples[:5]
    tuple2 = tuples [5:]
    print(tuple1)
    print(tuple2)
    # mid=(len(tuple) + 1) / 2
    # firstHalf = int(tuple[:mid])
    # secondHalf = int(tuple[mid:])






# 6. Create a program whose major task is to calculate an individual’s
# Net Salary by getting the inputs basic salary and benefits. Create 5 different functions which will calculate
# the payee (i.e. Tax), NHIFDeductions, NSSFDeductions, grossSalary and netSalary.  NB:Use KRA,
# NHIF and NSSF values provided online to find the appropriate deductions brackets on an individual’s gross salary.
def income(net):
    gross= input("please enter your gross salary")
    if gross >= 49057:
        tax= 0.3*gross
        net= gross- tax
        print(net)





# def greet():
#     print("Hello")
# greet()
# def greet():
#     greetings = "Hey you"
#     print(greetings)
# greet()

# def listofnumbers(ls):
#     newlist= ls[0], ls[-1]
#     return newlist
#
# list1= list(input("please enter a list "))
# extractedlist= listofnumbers(list1)
# print(extractedlist)
#
# type(list1)

# tuplelist= 1,2,3,4,5,6
# mid=(len(tuplelist) + 1) / 2
# print(tuplelist[:mid])
# firstHalf = int(tuplelist[:mid])
# secondHalf = int(tuplelist[mid:])
# print(firstHalf and secondHalf)

# print(tuplelist)
# print(len(tuplelist))
# tuple1= list(tuplelist)
# print(tuple1)
# print(len(tuple1))

# def max(X,Y,Z):
#     if X> Y and X> Z:
#         return(X)
#     elif Y> X and Y> Z:
#         return(Y)
#     elif Z> X and Z> Y:
#         return(Z)
#     elif X==Y and X>Z:
#         return(X)
#     elif Y==Z and Y>X:
#         return(Y)
#     elif X==Z and Z>Y:
#         return(Z)
#
#     else:
#         print("all numbers are equal")
#
# print(max(100,100,95))
# tuples = (1, 2, 3, 4, 5, 6, 7, 10, 23, 21,25)
# tuple1 = tuples[:int(len(tuples)/2)]
# tuple2 = tuples[int(len(tuples)/2):]
# print(tuple1)
# print(tuple2)

def taxes (salary):
    salary>=0
    if salary<= 12298:
        tax= int((salary*0.1)+400+200)
        return tax
    elif salary==12299 and salary<= 23885:
        tax= int((salary*0.15)+500+200)
        return tax
    else:
        return "tax not applicable"

salary = int(input("what is your salary"))
taxed= taxes(salary)
print(taxed)

# salary = int(input("What is your salary?"))
#
# print("So your gross annual salary is %r KSH" % (salary))
# print("\nNow we need to calculate what your net salary is.")
#
# def taxes(salary):
#
#     salary >= 0
#     if salary < 11000:
#         tax = 0
#     elif salary > 11000 and salary < 43000:
#         tax = (0.2 * income) - 2200
#     elif salary > 43000 and salary < 150000:
#         tax = (0.4 * (salary - 43000)) + 6400
#     elif salary > 150000:
#         tax = ((salary - 150000) * 0.45) + 6400 + 42800
#     else :
#         tax = undefined
#     return tax
# print(taxes(50000))


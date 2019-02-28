# y3= input("please enter a string:")
# if y3=="YES" or y3=="Yes" or y3=="yes":
#     print("yes")
# else:
#     print("no")

#3
def firstnlast(actely):
    new_list= [actely[0],actely[-1]]
    return new_list
lists= [1,2,3,4,5,6,7]
print(firstnlast(lists))

#4


def divisibility(num):
    if num % 4==0:
        return "multiple of 4"
    elif num % 2==0:
        return "even number"
    else:
        return "odd number"

number = int(input("Enter a number"))
print(divisibility(number))
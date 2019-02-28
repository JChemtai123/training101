# a while loop tells python to execute a certain or block of statements until a condition is met or until a condition is false
i= 0
#while i < 10:
    #print(i)
    #i= i+1
# i = 0
# while False:
#     print(i)
#     i= i+1

i= 0
# numbers= [0,1,2,3,4,5]
# while len(numbers)>0:
#     print(numbers)
#     numbers.pop()

while i<10:
     print("Actely")
     i+=1

password_saved = "1234"
password= input("Enter your password")
tries = 1
maxtries= 3
while password != "1234" and tries < 3:
    input("please enter correct password {} tries left". format(maxtries))
    #input("please enter correct password {} "+ maxtries")
    maxtries-=1
    tries +=1

if tries >= 3:
    print("Pin blocked, transaction withdrawn")
else:
    print("continue transaction")



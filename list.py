# initializing an empty string
emptystring = " "

print(type(emptystring))
# to initialize an integer
mynumber= 0
 # to initialize an empty list....
emptylist= []
crazy= ["Lizzy","Kate", 9, True]

daysOfTheWeek = ["Sunday","monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print(daysOfTheWeek)
no_of_days = print(len(daysOfTheWeek))
# list indexing
wednesday= daysOfTheWeek[3]
print(wednesday)
print(type(wednesday))
# 1:3, will start from position 1 to 3 but 3 is exclusive. The last index is always exclusive
mon_to_wed= daysOfTheWeek[3:3]
print(mon_to_wed)

details= ["Jacque",24,"jacque86@gmail.com", "Nairobi"]
age= details[1]
location= details[-1]
# print from reverse
reverse= details[::-1]
print("Reverse", reverse)
# print just the two in reverse
reverse2= reversed(details[2:3])
# there is -1,-2,-3
reverse= details[-2:4]
print(reverse)

numbers= [0,1,2,3,4,5,6,7,8,9,10]
sub_num= numbers[-3:-1]
print(sub_num)
reverse_num= numbers[-2:-4]
print(reverse_num)

# for unique type cast using set()

# appending/adding anything to a list
daysOfTheWeek.append("val")
print(daysOfTheWeek)
daysOfTheWeek.append(numbers)
print(daysOfTheWeek)

last_val_daysoftheweek= daysOfTheWeek[-1]
print(last_val_daysoftheweek)
# empty a list
#daysOfTheWeek.clear()
daysOfTheWeek.extend(numbers)
print(daysOfTheWeek)
# append adds to the list the way it is
# extend is like match it adds to you list
list1= [0,1]
list2 = [2,3]
list3= list1+list2
list1.append(list2)
list1.extend(list2)
print(list1)
print(list3)



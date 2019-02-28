# create a list and use inbuilt function sum..... just pass sum

student1Total= 85+82+78+65+66
student1= student1Total/5
student2Total = 73+42+84+52+55
student2= student2Total/5
student3Total= 55+74+92+86+100
student3= student3Total/5
student4Total= 20+21+75+58+87
student4= student4Total/5
print(student4)
student5Toal= 79+80+90+76+85
student5= student5Toal/5
print(student5)
studentMarks= [student1,student2, student3, student4,student5]

# do averages for each student and output the grade for each separately.....N/B class doing

for studentMark in studentMarks:
    if studentMark >= 80 and studentMark < 100:
        print("A")
    elif studentMark >= 70 and studentMark < 80:
        print("B")
    elif studentMark >= 60 and studentMark < 70:
        print("c")
    elif studentMark >= 50 and studentMark < 60:
        print("D")
    else:
        print("E")

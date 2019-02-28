# A class is a blueprint/prototype i.e. a collection of related properties and methods
class Student:
    # class variables are variables that are shared across all instances
    reg_number = ""
    grade = ""
    total= 0
    average = 0

    def __init__(self,math,eng,kis,sci,ssr):
        self.total =self.totalMarks(math,eng,kis,sci,ssr)
        self.calcAv(self.total)
    def totalMarks(self,math, eng, kis,sci,ssr):
      total= math+eng+kis+sci+ssr
      return total
    def calcAv(self,tot):
        self.average= tot/5
        return self.average

     # def calcgrade(self,grd):
     #     self.grade=


# variable actely is an object of a classmethod
# An object is an instance of a class
actely = Student(40,70,80,90,100)
kiki= Student(40,40,30,50,70)

print(actely.total)
print(actely.average)


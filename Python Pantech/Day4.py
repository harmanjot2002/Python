class Student:
    stuCount=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.stuCount+=1
    def displayCount(self):
        print("Total student %d" % Student.stuCount)
    def displayStudent(self):
        print("Name: ",self.name,"Age: ",self.age)
stu1 = Student("Sam",30)
stu2 = Student ("Manni",34)
stu1.displayStudent()
stu2.displayStudent()
print("Total students %d" % Student.stuCount)

class Parent:
    parentAttr=100
    def __init__(self):
        print("Calling parent constructor")
    def parentMethod(self):
        print("Calling parent method")
    def setAttr(self,attr):
        Parent.parentAttr=attr
    def getAttr(self):
        print("Parent attribute: ",Parent.parentAttr)
        
class Child(Parent):
    def __init__(self):
        print("Calling child constructor")
    def childMethod(self):
        print("Child class method")
c=Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
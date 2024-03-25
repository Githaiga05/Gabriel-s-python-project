#CLASSES  A Class is like an object constructor, or a "blueprint" for creating objects.

class Student:
    student_id = 0
    student_name = ""
    student_age = 0
    def __init__(self, id, name, age): #this is a constructor
        self.student_id = id #you just typed id thats why it's highlighted
        self.student_name = name
        self.student_age = age #self is the name of the class

    def displayStudent(self): #trying to output what is in the constructor
        print("The students details are: Name:", self.student_name, "Age:", self.student_age)


#This is a child constructor
#transfering data to the child constructor

class Person(Student):
    uniform="red"
    def __init__(self, id, name, age, uni):
        super().__init__(id,name,age)
        self.uniform = uni
        print("The student uniform is:", self.uniform)
#you can add details on the child constructor then add self of what you added

student1 = Student("100", "Smith", "20")
student1.displayStudent()
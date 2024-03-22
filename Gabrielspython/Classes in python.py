#CLASSES  A Class is like an object constructor, or a "blueprint" for creating objects.

class Student:
    student_id = 0
    student_name = ""
    student_age = 0
    def __init__(self, student_id, student_name, student_age): #this is a constructor
        self.student_id = id #you just typed id thats why it's highlighted
        self.student_name = student_name
        self.student_age = student_age #self is the name of the class

    def displayStudent(self): #trying to output what is in the constructor
        print("The students details are: Name:", self.student_name, "Age:", self.student_age)

student1 = Student("100", "Smith", "20")
student1.displayStudent()
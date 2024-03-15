#lists in python
'''
x.remove(x[4])# your removing element 5 in a list. Since (x[4]) is an index
'''

# Taking input of three student names
student_names = []
for i in range(3):
    name = input("Enter student name: ")
    student_names.append(name)

# Displaying the list of student names
print("List of student names:")
for name in student_names:
    print(name)

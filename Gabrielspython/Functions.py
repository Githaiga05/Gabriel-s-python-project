#finding largest number in a list
def my_function(*number):
    print("largest number is " , max(number))

my_function(10,20,9)


#adds items in a tuple
'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange, berry")
thistuple = tuple(y)

print(thistuple)
'''

#deletes lists of keys in a dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


#repeating values in an element
my_list = ["apple", "banana", "banana", "apple", "cherry"]
repeated_elements = []

for item in my_list:
    if my_list.count(item)>1:
        if item not in repeated_elements:
          repeated_elements.append(item)


print(repeated_elements)


#converting lists to dictionary
list1 = ["model", "year", "brand"]
list2 = ["harrier", "2020", "Toyota"]
print("My list1",list1)
print("My list2",list2)
mydict=dict(zip(list1,list2))
print("My dict",mydict)

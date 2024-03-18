thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#creatin taple with one item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#converting tuple to a list
fruits=("apple", "banana", "cherry", "apple", "cherry")
print(fruits)
myfruits = list(fruits) #convert tuple to a list
myfruits[1]="mangoes" #do your modification
myfruits.append("pineapple")
fruits=tuple(myfruits) #convert back to list


#SETS
# they don't allow duplicate values
#the lists are unordered
thisset = {"apple", "apple", "banana", "cherry"}
print(thisset)

#DICTIONARIES
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["model"]) #how to acces a model by giving the key
thisdict["model"] ="mustang" #modifying it
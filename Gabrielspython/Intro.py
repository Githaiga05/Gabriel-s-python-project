x=5
x+=3
x=x+3

print("my answer is:",x)

# == sign means equal to
x = 5
y = 3
print(x == y)

#!= means not equal to
x = 5
y = 3
print(x != y)

#if...elif statement
a = 200
b = 33
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")

#using the and statement
president_age=20
nationality="Ugandan"

if president_age > 18 and nationality=="Kenyan":
    print("You are a successful candidate")
else:
    print("You cannot be a candidate")

#checking if a number is odd or even
y=8
if y%2==0:
    print("Even")
else:
    print("Odd")

first_name="John"
last_name="Doe"
full_name=first_name+" "+last_name
print(full_name)

#converting integer(number) to a string (with speech marks)
#integer to string
first_name="John"
last_name=10
full_name=first_name+" "+str(last_name)#string is clamping them together
print(full_name)

#string to integer
pens_total=40
books_total="50"
grand_total=int(books_total)+pens_total#init is adding them
print("my overall total is:" ,grand_total)

#float to string
bucket=20.0 #Is a float
book="50.0"
total=bucket+float(book)
result="The total is:"+str(total)+" kenyan shillings"
print(result)

#LOOPING IN PYTHON
#The while loop
i = 1
while i < 6:
  print(i)
  i += 1

  #break stops the loop
i = 1
while i < 6:
  print("the value of i is ",i)
  if i == 3:
    break
  i += 1

#the continue statement in the while loop
  i = 1
  while i < 6:
      i += 1
      if i == 3: #if 3 is equals to 3 it jumps it
          continue
      print("the answer is",i)
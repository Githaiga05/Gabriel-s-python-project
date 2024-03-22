#The try block will generate an error, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")


  # The try block does not raise any errors, so the else block is executed:
try:
  print("Hello")
except:
 print("Something went wrong")
else:
  print("Nothing went wrong")


#The finally block gets executed no matter if the try block raises any errors or not:
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")







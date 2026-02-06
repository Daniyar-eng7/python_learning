fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  
  #loop through a string
  for x in "banana":
  print(x)
  
    #the break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#the continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
  #the range() function
  for x in range(6):
    print(x)
  
  #the range() function with start and end parameters
  for x in range(2, 6):
     print(x)
    
    #the range() function with step parameter
for x in range(2, 30, 3):
     print(x)
     
     #else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
  
  
    #pass statement
for x in [0, 1, 2]:
   pass

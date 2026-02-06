# Example of if statement
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
  
  #variable condition
is_logged_in = True
if is_logged_in:
  print("Welcome back!")
 
 # elif statement example 
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
  
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
  
  
  
  #Categorizing age groups:

age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")
  
  #example number to day of the week
  day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")
  
 #else statement example 
  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  #else statement example
  a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
  
  #short hand if statement
  a = 5
b = 2
if a > b: print("a is greater than b")


#short hand if else statement
a = 2
b = 330
print("A") if a > b else print("B")


#short hand if else statement with more conditions
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#multiple conditions in short hand if else statement
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#logical operators with if statements
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
  #logical operators with if statements
  a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
  
  #not operator with if statement
  a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
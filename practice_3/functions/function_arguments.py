# Function Arguments
def func(fname):
    print(fname + " Refsnes")
    
func("Emil")
func("Tobias")
func("Linus")

# Parameters and Arguments
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument


# Number of Arguments
def func(fname, lname):
    print(fname + " " +lname)
func("Emil", "Refsnes")


# Default Arguments
def func3(name = "friend"):
    print("hello, "+ name)
func3("Emil")
func3() # default value is used when no argument is provided

# Default Arguments
def func4(country = "Norway"):
    print("I am from " + country)
func4("Sweden")
func4("India") 
func4() # default value is used when no argument is provided


# Keyword Arguments
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
my_function(animal = "dog", name = "Willie")


# Keyword Arguments can be called in any order
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")


# If you use keyword arguments, the order of the arguments does not matter.
def fun3(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)
fun3(animal="dog", name="Buddy", age=5)


#Sending a list as an argument:
def func5(fruits):
    for x in fruits:
        print(x)
fruits= ["apple", "banana", "cherry"]
func5(fruits)




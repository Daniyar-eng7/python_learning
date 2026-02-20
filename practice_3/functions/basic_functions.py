# calling a function
def func():
    print("hello")

func()

# repeat a function
def change_func(far):
    return (far -32) *5/9

print(change_func(77))


# function with return value
def func2():
    return("hello")
message = func2()
print(message)



#Using the return value directly:
def get_greeting():
  return "Hello from a function"

print(get_greeting())


#pass statement
def func3():
    pass
#concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c) # Hello World

#Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Display the price multiplied by 28:
txt = f"The price is {28 * 59} dollars"
print(txt)
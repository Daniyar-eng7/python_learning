#boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)


#variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#comparison operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#logical operators
x = 5
print(x > 0 and x < 10)
print(x < 5 or x > 10)


#identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #t
print(x is y) #f
print(x is not y) #t
print(x == y)

#membership operators
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("pineapple" not in fruits)


#bitwise operators
a = 60  # 0011 1100
b = 13  # 0000 1101
print(a & b)  # AND # 0000 1100 = 12
print(a | b)  # OR  # 0011 1101 = 61
print(a ^ b)  # XOR # 0011 0001 = 49
print(~a)     # NOT # 1100 0011 = -61
print(a << 2) # Left Shift  # 1111 0000 = 240
print(a >> 2) # Right Shift # 0000 1111 = 15


#boolean functions
print(bool("Hello"))  #t   
print(bool(15))         

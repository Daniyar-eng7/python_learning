#function
def my_power(x, y):
    return x ** y

#lambda
my_power = lambda x, y: x ** y
print(my_power(2, 3))  # 8


x = lambda a : a + 10
print(x(5))


x= lambda a, b, c: a+b+c
print(x(1,4,6))

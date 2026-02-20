
#lambda with map
nums= [34, 54, 32, 4]
x=map(lambda nums: x**2, nums)
print(list(x))

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


#lambda with filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd=list(filter(lambda x: x%2!=0 ,numbers))
print(odd)


list1 = [2, 3, 5, 8, 16, 100, 103]
list2 = list(filter(lambda x: x % 2 == 0, list1))
print(list2)  # [2, 8, 16, 100]


#prime numbers
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

list1 = [1, 2, 14, 5, 13, 100, 103]
list2 = list(filter(lambda x: is_prime(x), list1))
print(list2)  # [2, 5, 13, 103]



#sort by age
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)



#Sort strings by length:
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
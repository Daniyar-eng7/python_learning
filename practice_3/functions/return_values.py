def f(a, b):
    result1 = a * b
    result2 = a + b
    result3 = a - b
    return result1, result2, result3

a, b, c = f(2, 3)
a, _, _ = f(2, 3)  # only need first value
_, a, _ = f(2, 3)  # only need second value
a, _, c = f(2, 3)  # need first and third
print(a, c)




#recursion
result = dict()

def rec(n):
    if n in result:
        return result[n]

    if n == 0 or n == 1:
        return 1
    result[n] = rec(n - 1) + rec(n - 2)
    return result[n]

print(rec(5))
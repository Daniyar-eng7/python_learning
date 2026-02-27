#1-task
"""
def gen(n):
    lis=[]
    i=0
    while i<n:
        i+=1
        yield i**2
        
n=int(input())

for i in gen(n):
    print(i)
"""


#2-task
'''
num=int(input())

def gen(n):
    for i in range(n+1):
        if i%2==0:
            yield i

print(*gen(num), sep=', ')
'''


#3-task
'''
num=int(input())

def gen(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i

print(*gen(num), sep=", ")
'''

'''
a=int(input())
b=int(input())

def squares(a, b):
    for i in range(a, b+1):
        yield i**2

print(*squares(a,b), sep=", ")
'''

#5-task
num=int(input())

def gen(a):
    for i in range(a, -1, -1):
        yield i

print(*gen(num), sep=", ")
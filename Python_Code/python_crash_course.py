from random import choice
from functools import partial
import random




def lzrange(n):
    i=0
    while i < n:
        yield i
        i+=1

random.choice(["Alice", "Bob", "Charlie"]) 
sample=random.sample(range(10),5)

def exp(number, power):
    return number ** power

two_to_the = partial(exp, 2)
square_of = partial(exp, power=2)
three_to_the = lambda x: exp(3, x)

two_to_the(5)
square_of(7)
three_to_the(3)

def double(x):
    return 2 * x

# mapping
ls=list
xs = [1, 2, 3, 4]
twice_xs=[double(x) for x in xs]
alter_twice_xs=ls(map(double, xs))
alter_twice_func=partial(map, double)
alter_twice_lam = lambda x: ls(map(double, x))

# zipping and unpacking
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
pairs=zip(list1, list2) 
unzip=ls(zip(*pairs))

add=lambda x,b:x+b

def doubler(f):
 def g(x):
    return 2 * f(x)
 return g


def f1(x):
 return x + 1
g = doubler(f1)
#print (g(3)) # 8 (== ( 3 + 1) * 2)
#print (g(-1) )

def mult(no):
    return no * 2

def addi(no):return no + 2

def add_up(x):
    add=x(5)
    print(add)

def square(f):
    def g(x):
        return x * f(x)
    return g

def ret(y):
    return y+2

g = square(ret)
print(g(2))

"""There are two primary uses for data visualization:
• To explore data
• To communicate data"""

def magic(*args, **kwargs):
    print("unnamed args: ", args)
    print("named args: ", kwargs)
magic(1,2,key="word", key2="word")


"""
-Partial functions allow us to fix a certain no. of arguments of a function and generate a new function.
-Partial functions can be used to derive specialied functions from general functions and therefore help us to reuse our code.
-Using partial function is a concept of metaprogramming in Python,a concept that refers to a programmer writing code that manipulates code.
"""
from functools import partial
def f(a,b,c,x):
    return 1000*a+100*b+10*c+x

g=partial(f,3,1,4)
print(g(5))

#In this,we have pre-filled our function with some constant values of a,b,c and g() takes single arg(x)

from functools import *

def add(a,b,c):
    return 100*a+10*b+c

add_part=partial(add,c=2,b=1)
print(add_part(3))

#Nested Functions
def outerFunction(text):
    text=text
    def innerFunction():
        print(text)
    innerFunction()
if __name__=='__main__':
    outerFunction('Hey!')

#Closures
#A closure allows the function to access those captures variables through the closure's copies of their values of references,even when function is invoked outside their scope.
#Closures help to invoke functions outside their scope.
#

def outerFunction(text):
    text=text
    def innerFunction():
        print(text)
    return innerFunction
if __name__=="__main__":
    myFunction=outerFunction("Hey!")
    myFunction()


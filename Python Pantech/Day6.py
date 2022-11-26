# package is a folder containing one or more modules.
# Use of __init__.py:
#     Python interpreter recognizes a folder as a package if it contains __init__.py file.
#     __init__.py exposes specfied resources from its modules to be imported.
#     An empty __init__.py file makes all functions from the above modules available when this package is imported.

# generator function is similar to normal functions,but whenever it needs to generate a value,it does so with yield keyword rather than return keyword. 

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)

# Generator functions return a generator object.
# Generator objects are used either by calling the next method on the generator object or using the generator object in a "for in" loop.

# Iterting over the generator object using "next"
x=simpleGeneratorFun()
print(next(x))
print(next(x))
print(next(x))
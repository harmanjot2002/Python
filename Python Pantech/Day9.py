#Decorators are a powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class.
#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,without permanently modifying it.

#1.Functions can be treated as objects.
def shout(text):
    return text.upper()
print(shout("Hello"))
yell=shout
print(yell("Hello"))

#2.Passing function as an argument to another function
def whisper(text):
    return text.lower()
def greet(func):
    greeting=func("""Hi I am created by a function passed as an argument""")
    print(greeting)
greet(shout)
greet(whisper)

#3.Returning function from another function
def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15=create_adder(15)
print(add_15(10))

#4.Functions are taken as the argument into another function and then called inside the wrapper function.
# @gfg_decorator
# def hello_decorator():
#     print("Gfg")
'''Above code is equivalent to-
def hello_decorator():
    print("Gfg")
hello_decorator=gfg_decorator(hello_decorator)'''
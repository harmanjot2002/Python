#Decorators are a powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class.
#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,without permanently modifying it.

#1.Functions can be treated as objects.
def shout(text):
    return text.upper()
print(shout("Hello"))
yell=shout
print(yell("Hello"))



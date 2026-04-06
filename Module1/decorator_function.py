# Decorators let you add extra behavior to a function, without changing the function's code.
def makeUpper(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@makeUpper
def printName(name):
    return name

name = input("Write your name: ")
print(printName(name))

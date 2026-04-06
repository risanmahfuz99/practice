# Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.
# The code inside the function is not executed yet, it is only compiled.
# The function only executes when you iterate over the generator.

#use case: Used to get elements without storing
def getTopVal():
    n=1
    while(n<=10):
        yield n*n
        n=n+1

values=getTopVal()
for i in values:
    print(i)
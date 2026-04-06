def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23,23]

thislist.sort(key = myfunc)

print(thislist)

numlist = thislist
print(numlist)

# copy and new tupple
newTupple = tuple(numlist)
print(newTupple)
print(type(newTupple))
print(newTupple[0])
newTupple = (10,20,30,40)
tempTupple=(50,60)
newTupple += tempTupple
print(newTupple)

# asterisk operator
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)







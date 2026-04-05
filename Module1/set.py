# set
newSet = {1,2,3,4,5}

# for x in newSet:
#   print(x)
print ( 3 in newSet)
newSet.add(6)
tempSet={7,8,9}
newSet.update(tempSet) # set can be updated
print(newSet)

# remove and discard in set
# if remove is used and no element is present as the given element it gives an error
# but discard wont give error

# newSet.remove(8)
# newSet.discard(8)
# newSet.discard(8)
print(newSet)
# newSet.remove(8)
# newSet.discard(8)

#Remove a random item by using the pop() method:
newSet.pop()
newSet.pop()
print(newSet)

# set can perform | & ^ difference , symmetric_difference

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

# frozen set is immutable
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
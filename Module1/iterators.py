mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
#
# print(next(myit))
# print(next(myit))
# print(next(myit))


# this loop
# for fruit in mytuple:
#     print(fruit)

# is exactly same as this
myit = iter(mytuple)
while True:
    try:
        print(next(myit))
    except StopIteration:
        break
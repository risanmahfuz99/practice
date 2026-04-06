def singleMultiplication(n):
  return lambda a : a * n

mydoubler = singleMultiplication(2)
mytripler = singleMultiplication(3)

print(mydoubler(11))
print(mytripler(11))

def listMultiplication(lists):
  return list(map(lambda a : a * 2, lists))
lists = listMultiplication([1,2,3,4,5])
print(lists)
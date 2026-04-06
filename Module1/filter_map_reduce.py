from functools import reduce
# filter
nums = [1,2,3,4,5,6,7,8,9,10]
# print(nums)
oddNums = list(filter(lambda n:n%2==1, nums))
print(oddNums)

# map

doubleOddNums = list(filter(lambda n:n*2, oddNums))
print(doubleOddNums)

#reduce
sumOddNums= reduce(lambda x,y:x+y, oddNums)
print(sumOddNums)   
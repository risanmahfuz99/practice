# in operator checks  an element is in the object

students = ["joy" , "limon", "jaher" ,"rezo"]
if "joy" in students:
    print("In")
else :
    print("Out")

[print(x) for x in students]
newlist = [x in x for x in students if 'a' in x]
# newlist=[]
# for x in students:
#     if 'o' in x:
#         newlist.append(x)
#

students.sort()
print(students)

newlist.sort(reverse=True)
print(students)


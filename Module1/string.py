import re
from fnmatch import translate

name="Not Bob"
print(name)


print("It's alright")
print("The name is 'Bond', 'James Bond'.") # print with quotes

# finding a word in a string
text = "There soul should have been obliterated by now. So there shall be no eden left."
if "soul" in text:
    print("Soul is present")
else:
    print("Soul is not present")

print("Bond" not in text)

# first parameter is inclusive and the last one is exclusive
print(text[2:7])
print(text[:2])
print(text[2:])
print(text[:])
print(text[-5:-2])  #-1 is the last index

print(text.replace("T","x")) #replace is case-sensitive
# use re for case-insensitive
result = re.sub("T", "x", text, flags=re.I)
print(result)

# formatting
salary = 100
print (f"salary is {salary}")


# transalation
text = "hello world"
table = str.maketrans("aeiou", "12345") #replace
print(text.translate(table))  # Output: h2ll4 w4rld

text = "hello world"
table = str.maketrans("", "", "aeiou")  # third arg = chars to delete
print(text.translate(table))  # Output: hll wrld

text = "hello world"
table = str.maketrans("hw", "HW", "aeiou")  # replace h→H, w→W and delete vowels
print(text.translate(table))  # Output: Hll Wrld

#split
# csv_row = "1,2,3,4,5,6"
# fields = csv_row.split(" ")
csv_row = "1 2 3 4 5 6"
fields = csv_row.split(" ")
print(fields)
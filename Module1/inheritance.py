# single
class Animal:
    def breathe(self):
        return "Breathing..."

class Dog(Animal):
    def bark(self):
        return "Woof!"

d = Dog()
print(d.breathe())
print(d.bark())


# multilevel
class Dog(Animal):
    def bark(self):
        return "Woof!"

class Puppy(Dog):
    def weep(self):
        return "Whimpering..."

p = Puppy()
print(p.breathe())
print(p.bark())
print(p.weep())


## multiple
class Father:
    def coding(self):
        return "Loves coding"

class Mother:
    def cooking(self):
        return "Loves cooking"

class Child(Father, Mother):   # inherits from both
    def sports(self):
        return "Loves sports"

c = Child()
print(c.coding())
print(c.cooking())
print(c.sports())

# hierarchical

class Dog(Animal):
    def bark(self):
        return "Woof!"

class Cat(Animal):
    def meow(self):
        return "Meow!"

class Bird(Animal):
    def chirp(self):
        return "Tweet!"

d = Dog()
c = Cat()
b = Bird()

print(d.breathe())
print(c.breathe())
print(b.breathe())


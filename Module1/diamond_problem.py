class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog speaks"

class Cat(Animal):
    def speak(self):
        return "Cat speaks"

class Hybrid(Dog,Cat):
    pass

h = Hybrid()
print(h.speak())
print(Hybrid.mro())
from abc import ABC, abstractmethod
class Computer:
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print("Laptop")

device = Laptop()
device.process()
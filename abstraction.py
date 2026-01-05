from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
# Concrete subclass
class Car(Vehicle):
    def start(self):
        print("Car engine started.")

    def stop(self):
        print("Car engine stopped.")


# Concrete subclass
class Bike(Vehicle):
    def start(self):
        print("Bike engine started.")

    def stop(self):
        print("Bike engine stopped.")


# Using the classes
if __name__ == "__main__":
    vehicles = [Car(), Bike()]
    for v in vehicles:
        v.start()
        v.stop()

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         # This special method defines the behavior of the '+' operator.
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
# v1 = Vector(2, 3)
# v2 = Vector(4, 5)
# v3 = v1 + v2
#
# print(v3)
# CLASSES AND OBJECTS
# -------------------
# A class is a blueprint. An object is an instance built from that blueprint.
#
# Real-world analogy:
#   Class  = the blueprint for a house (defines rooms, dimensions, features)
#   Object = an actual house built from that blueprint
#
# You can build many houses from one blueprint — each is its own object
# with its own state (paint color, furniture) but the same structure.
#
# In Python, EVERY value is an object — int, str, list, etc. are all
# classes built into the language. When you write x = 42, you're creating
# an instance of the int class.

# DEFINING A CLASS
class Dog:
    # __init__ is the constructor — runs when a new object is created
    # self refers to the specific instance being created
    def __init__(self, name, breed):
        self.name = name       # instance attribute — unique to each object
        self.breed = breed

    # A method — a function that belongs to the class
    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} is a {self.breed}")


# CREATING OBJECTS (instantiation)
dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Bella", "Poodle")

# Each object has its own state
print(dog1.name)    # Rex
print(dog2.name)    # Bella

# Calling methods
dog1.bark()         # Rex says: Woof!
dog2.describe()     # Bella is a Poodle

# type() confirms these are instances of Dog
print(type(dog1))             # <class '__main__.Dog'>
print(isinstance(dog1, Dog))  # True

# __main__ is the name Python gives to the file you ran directly.
# When you run `python 01_what_is_a_class.py`, Python sets that file's
# __name__ to "__main__", so Dog defined here becomes __main__.Dog.
# If Dog were defined in a file called animals.py and imported, you'd
# see <class 'animals.Dog'> instead.
#
# This leads to the most common Python idiom:
if __name__ == "__main__":
    # Code here only runs when this file is executed directly.
    # It is skipped when the file is imported by another module.
    # Use it to separate reusable code (classes, functions) from
    # script-specific startup logic.
    dog1.bark()

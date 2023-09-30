'''
Q5.What is method overriding in python? 
Write a python code to demonstrate method overriding.
'''

class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Dog barks.")

class Cat(Animal):
    def sound(self):
        print("Cat meows.")

# Creating objects of different classes
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the sound method of each object
animal.sound()  # Output: Animal makes a sound.
dog.sound()     # Output: Dog barks.
cat.sound()     # Output: Cat meows
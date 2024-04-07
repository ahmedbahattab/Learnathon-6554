class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Testing the classes
animal = Animal()
animal.speak()  # Output: Animal speaks

dog = Dog()
dog.speak()  # Output: Dog barks

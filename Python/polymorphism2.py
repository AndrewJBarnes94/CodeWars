class Animal:
    def sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Create objects of different classes
animal_obj = Animal()
dog_obj = Dog()
cat_obj = Cat()

# Polymorphism in action
print(animal_obj.sound())  # Output: Generic animal sound
print(dog_obj.sound())     # Output: Bark!
print(cat_obj.sound())     # Output: Meow!

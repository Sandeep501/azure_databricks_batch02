# Inheritense with polymorphism

class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes sound"
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks"
    
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} meows"

tommy = Dog("tommy", "xyz")
print(tommy.speak())

mufasa = Cat("Mufasa", "White")
print(mufasa.speak())


  

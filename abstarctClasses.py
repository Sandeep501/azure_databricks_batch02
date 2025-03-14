from abc import ABC, abstractmethod, abstractclassmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    
    def start_engine(self):
        return "Car engine has started"
    
    def stop_engine(self):
        return "Car engine has stopped"
    
    def details(self):
        return f"I drive BMW"
    
car_inst = Car()
print(car_inst.details())

vahicle = Vehicle()
print(Vehicle.start_engine())
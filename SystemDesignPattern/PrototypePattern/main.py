'''
Implementation of prototype design pattern
'''

from abc import abstractmethod,ABC
import copy

#Prototype Interface
class Prototype(ABC):
    
    @abstractmethod
    def clone(self):
        """
        Abstract method to be implemented by concrete prototypes.
        Ensures that all subclasses implement a 'clone' method.
        """
        pass

#Concrete Class1
class Car(Prototype):
    def __init__(self, model, color, engine_power):
        self.model = model
        self.color = color
        self.engine_power = engine_power

    def __str__(self):
        return f'Car(Model: {self.model}, Color: {self.color}, Engine Power: {self.engine_power})'

    def clone(self):
        # Using deepcopy to clone the object
        return copy.deepcopy(self)

# Concrete Prototype 2
class Truck(Prototype):
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

    def __str__(self):
        return f'Truck(Model: {self.model}, Capacity: {self.capacity} tons)'

    def clone(self):
        # Using deepcopy to clone the object
        return copy.deepcopy(self)        
    
#Client Code
if __name__ == "__main__":
    # Creating original objects (prototypes)
    car1 = Car("Tesla Model 3", "Red", "250hp")
    truck1 = Truck("Ford F-150", 5)

    print("Original objects:")
    print(car1)
    print(truck1)

    # Cloning the objects
    car2 = car1.clone()
    truck2 = truck1.clone()

    print("\nCloned objects:")
    print(car2)
    print(truck2)

    # Modifying the cloned objects
    car2.color = "Blue"
    truck2.capacity = 10

    print("\nModified cloned objects:")
    print(car2)
    print(truck2)

    print("\nOriginal objects remain unchanged:")
    print(car1)
    print(truck1)
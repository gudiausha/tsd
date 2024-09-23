from abc import ABC, abstractmethod

# Component Interface (or base class)
class Wrapee(ABC):
    '''
    This is the class on which wrappers are made - the first base object
    '''
    @abstractmethod
    def msg(self):
        pass

# Concrete Component
class ConcreteWrapee(Wrapee):
    '''
    Concrete implementation of the base Wrapee object
    '''
    def msg(self):
        print('Hello, I am the base object method - ConcreteWrapee. Say Hi to me!')

# Base Decorator
class BaseDecorator(Wrapee):
    '''
    Base decorator class that wraps around the Wrapee. Other decorators will inherit from this.
    '''
    def __init__(self, wrapee: Wrapee) -> None:
        self._wrapee = wrapee

    def msg(self):
        # Pass the call to the wrapped component (Wrapee)
        self._wrapee.msg()

# Concrete Decorator 1
class Decorator1(BaseDecorator):
    def __init__(self, wrapee: Wrapee) -> None:
        super().__init__(wrapee)

    def msg(self):
        print('Decorator 1: Adding extra behavior before calling base Wrapee')
        super().msg()  # Call the base wrapee msg method
        print('Decorator 1: Adding extra behavior after calling base Wrapee')

# Concrete Decorator 2
class Decorator2(BaseDecorator):
    def __init__(self, wrapee: Wrapee) -> None:
        super().__init__(wrapee)

    def msg(self):
        print('Decorator 2: Adding extra behavior before calling base Wrapee')
        super().msg()
        print('Decorator 2: Adding extra behavior after calling base Wrapee')

if __name__ == '__main__':
    # Create the base Wrapee object
    base_obj = ConcreteWrapee()

    # Wrap the base object with Decorator 1
    decorated_obj_1 = Decorator1(base_obj)
    decorated_obj_1.msg()

    print()

    # Further wrap the object with Decorator 2
    decorated_obj_2 = Decorator2(decorated_obj_1)
    decorated_obj_2.msg()

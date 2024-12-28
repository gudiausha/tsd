'''
Contains code after the implementation of the Strategy pattern

strategy_obj --> Passed to every child class so that different strategies can be passed to different objs
MainBaseClass --> referenced as Context Class
'''
from strategy_implementation import strategy_obj1,strategy_obj2

class MainBaseClass():
    def __init__(self) -> None:
        self.strategy_obj = None

    def set_strategy(self, strategy_obj):
        '''
        Allows to dynamically change the strategy obj
        '''
        self.strategy_obj = strategy_obj
    
    def A(self):
        print('Hi I am Class A from the Base Class')

    def B(self):
        print('Hi I am Class B from the Base Class')

class ChildClass1(MainBaseClass):
    def __init__(self) -> None:
        super().__init__()

    def C(self):
        print('Hi I am Class C from the Child Class1')

    def B(self):
        if self.strategy_obj:
            self.strategy_obj.B()
        else:
            super().B()

    def H(self):
        self.strategy_obj.H()

class ChildClass2(MainBaseClass):
    def __init__(self) -> None:
        super().__init__()

    def D(self):
        print('Hi I am Class D from the Child Class2')

    def A(self):
        self.strategy_obj.A()

    def H(self):
        self.strategy_obj.H()

class ChildClass3(MainBaseClass):
    def __init__(self) -> None:
        super().__init__()

    def E(self):
        print('Hi I am Class E from the Child Class3')

    def B(self):
        self.strategy_obj.B()

    def H(self):
        self.strategy_obj.H()

class ChildClass4(MainBaseClass):
    def __init__(self) -> None:
        super().__init__()

    def F(self):
        print('Hi I am Class F from the Child Class4')

    def A(self):
        self.strategy_obj.A()

    def H(self):
        self.strategy_obj.H()

if __name__ == '__main__':
    # Create a child class instance without passing a strategy
    child_class_instance = ChildClass1()

    print("Without setting any strategy:")
    child_class_instance.B()  # Will print "'Hi I am Class B from the Base Class'"

    # Dynamically assign a strategy using set_strategy
    child_class_instance.set_strategy(strategy_obj1)

    print("\nAfter setting strategy1 (ConcreteClass1):")
    child_class_instance.B()  # Will print B() from ConcreteClass1
    child_class_instance.H()  # Will print H() from ConcreteClass1

    # Change the strategy at runtime to ConcreteClass2
    child_class_instance.set_strategy(strategy_obj2)

    print("\nAfter changing to strategy2 (ConcreteClass2):")
    child_class_instance.B()  # Will print B() from ConcreteClass2
    child_class_instance.H()  # Will print H() from ConcreteClass2
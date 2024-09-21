"""
As part of the strategy pattern, an interface and abstract methods are created. 
The concrete class implement these methods. 
And they are called in main.py, where each subclass can choose which concrete method to call according to the usecase.
"""
from abc import ABC,abstractmethod

class StrategyPatternInterface(ABC):
    '''
    Contains only defintion, no implementation
    '''

    @abstractmethod
    def A(self):
        pass

    @abstractmethod
    def B(self):
        pass

    @abstractmethod
    def H(self):
        pass

class ConcreteClass1(StrategyPatternInterface):
    '''
    Contains implementation of the abstract methods
    '''

    def A(self):
        print('Hi I am Class A and will be same in Class2 and Class4. Uff I have been overridden')

    def B(self):
        print('Hi I am Class B and will be same in Class1 and Class3. Uff I have been overridden')

    def H(self):
        print('Hi I am Class H. I am not dereieved from Base Class. I am common in Classes 1-4 ')

class ConcreteClass2(StrategyPatternInterface):
    def A(self):
        print('Hi, this is an alternate implementation of A')

    def B(self):
        print('This is another implementation of B')

    def H(self):
        print('Alternate implementation of H')


strategy_obj1 = ConcreteClass1()
strategy_obj2 = ConcreteClass2()
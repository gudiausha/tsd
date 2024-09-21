'''
Contains code after the implementation of the Strategy pattern
'''
from strategy_implementation import strategy_obj

class MainBaseClass():
    def __init__(self,strategy_obj) -> None:
        self.strategy_obj = strategy_obj
    
    def A(self):
        print('Hi I am Class A from the Base Class')

    def B(self):
        print('Hi I am Class B from the Base Class')

class ChildClass1(MainBaseClass):
    def __init__(self) -> None:
        super().__init__(strategy_obj)

    def C(self):
        print('Hi I am Class C from the Child Class1')

    def B(self):
       strategy_obj.B() 

    def H(self):
        strategy_obj.H()

class ChildClass2(MainBaseClass):
    def __init__(self) -> None:
        super().__init__(strategy_obj)

    def D(self):
        print('Hi I am Class D from the Child Class2')

    def A(self):
        strategy_obj.A()

    def H(self):
        strategy_obj.H()

class ChildClass3(MainBaseClass):
    def __init__(self) -> None:
        super().__init__(strategy_obj)

    def E(self):
        print('Hi I am Class E from the Child Class3')

    def B(self):
        strategy_obj.B()

    def H(self):
        strategy_obj.H()

class ChildClass4(MainBaseClass):
    def __init__(self) -> None:
        super().__init__(strategy_obj)

    def F(self):
        print('Hi I am Class F from the Child Class4')

    def A(self):
        strategy_obj.A()

    def H(self):
        strategy_obj.H()

if __name__ == '__main__':
    main_class_output = MainBaseClass(strategy_obj)
    child_class_output = ChildClass1()
    main_class_output.B()
    child_class_output.B()
    child_class_output.H()
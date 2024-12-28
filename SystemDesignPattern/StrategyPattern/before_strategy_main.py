'''
Contains code before the implementation of the Strategy pattern

Conclusion.: 
If we see the code among various sub classes is similar and this leads to code duplicacy. 
The strategy pattern helps to solve that.
'''

class MainBaseClass():
    def __init__(self) -> None:
        pass
    
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
        print('Hi I am Class B and will be same in Class1 and Class3. Uff I have been overridden')

    def H(self):
        print('Hi I am Class H. I am not dereieved from Base Class. I am common in Classes 1-4 ')

class ChildClass2(MainBaseClass):
    def __init__(self) -> None:
        super().__init__()

    def D(self):
        print('Hi I am Class D from the Child Class2')

    def A(self):
        print('Hi I am Class A and will be same in Class2 and Class4. Uff I have been overridden')
    
    def H(self):
        print('Hi I am Class H. I am not dereieved from Base Class. I am common in Classes 1-4 ')

class ChildClass3(MainBaseClass):
    def __init__(self) -> None:
        super().__init__()

    def E(self):
        print('Hi I am Class E from the Child Class3')

    def B(self):
        print('Hi I am Class B and will be same in Class1 and Class3. Uff I have been overridden')

    def H(self):
        print('Hi I am Class H. I am not dereieved from Base Class. I am common in Classes 1-4 ')

class ChildClass4(MainBaseClass):
    def __init__(self) -> None:
        super().__init__()

    def F(self):
        print('Hi I am Class D from the Child Class4')

    def A(self):
        print('Hi I am Class A and will be same in Class2 and Class4. Uff I have been overridden')

    def H(self):
        print('Hi I am Class H. I am not dereieved from Base Class. I am common in Classes 1-4 ')

if __name__ == '__main__':
    main_class_output = MainBaseClass()
    child_class4_output = ChildClass4()
    main_class_output.B()
    child_class4_output.B()
    child_class4_output.A()

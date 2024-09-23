class Wrapee():
    '''
    This is the base class without using decorators.
    All additional functionalities would need to be hardcoded.
    '''
    def __init__(self) -> None:
        pass

    def msg(self):
        print('Hello I am the base object method - Wrapee. Say Hi to me!')

class ExtendedWrapee(Wrapee):
    '''
    A class extending the Wrapee functionality without decorators.
    We hardcode the new behavior directly into the class.
    '''
    def msg(self):
        print('Adding extra behavior before calling base Wrapee')
        super().msg()  # Call the base Wrapee msg method
        print('Adding extra behavior after calling base Wrapee')

class AnotherExtendedWrapee(Wrapee):
    '''
    Another class extending the Wrapee functionality without decorators.
    Each class adds behavior in its own way, but there's no flexible composition like in decorators.
    '''
    def msg(self):
        print('Another extension of Wrapee - Additional behavior before')
        super().msg()
        print('Another extension of Wrapee - Additional behavior after')

if __name__ == '__main__':
    # Use the base object
    base_obj = Wrapee()
    base_obj.msg()

    print()

    # Use the extended object
    extended_obj = ExtendedWrapee()
    extended_obj.msg()

    print()

    # Use another extended object
    another_extended_obj = AnotherExtendedWrapee()
    another_extended_obj.msg()

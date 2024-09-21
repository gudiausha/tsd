'''
Implement the subscriber interface and subscriber concrete class.
'''
from abc import ABC,abstractmethod

class SubscriberInterface(ABC):

    @abstractmethod
    def subscriber_update(self,state_value):
        pass

class SubscriberConcreteClass1(SubscriberInterface):
    '''
    Subscriber class for Email Publisher
    '''
    def subscriber_update(self,state_value=0):
        print('Hi I am Subscriber of Subscriber Class 1. Notification Acknowledged')

class SubscriberConcreteClass2(SubscriberInterface):
    '''
    Subscriber class for SMS Publisher
    '''
    def subscriber_update(self,state_value):
        print(f'The state value is - {state_value}')
        if state_value > 3:
            print('Hi I am Subscriber 2. Notification Acknowledged')
        else:
            print('Notification Not Acknowledged')


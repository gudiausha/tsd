'''
Implement the publisher interface and publisher concrete class.
'''
from abc import ABC,abstractmethod
from random import randrange

class PublisherInterface(ABC):

    @abstractmethod
    def add_subscribers(self,subscriber_obj):
        pass

    @abstractmethod
    def unsubscribe(self,subscriber_obj):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def list_subscribers(self):
        pass

class PublisherConcreteClass1(PublisherInterface):
    '''
    Assume this to be Email Publisher
    '''

    def __init__(self) -> None:
        '''
        Instead of a list, in real implementation can have it as [dictionary].
        {key:value} = {unique_id:email/phone}
        This would allow to easy update whenever the email/phone of subscriber is updated
        '''
        self._subscribers_list = []

    def add_subscribers(self,subscriber_obj):
        self._subscribers_list.append(subscriber_obj)
        print('Successfully Subscribed')

    def unsubscribe(self,subscriber_obj):
        self._subscribers_list.remove(subscriber_obj)
        print('Successfully removed subscription')

    def notify(self):
        for subscriber_obj in self._subscribers_list:
            print('Hello I am Email Publisher. Sending an update.')
            subscriber_obj.subscriber_update()

    def list_subscribers(self):
        for subscriber_obj in self._subscribers_list:
            print(subscriber_obj)

    def business_logic_update(self,update_keyword):
        if update_keyword == 'Notify my subscribers':
            self.notify()
        else:
            print('No notification to be sent')

class PublisherConcreteClass2(PublisherInterface):
    '''
    Assume this to be SMS Publisher
    '''

    def __init__(self) -> None:
        '''
        Instead of a list, in real implementation can have it as [dictionary].
        {key:value} = {unique_id:email/phone}
        This would allow to easy update whenever the email/phone of subscriber is updated
        '''
        self._subscribers_list = []
        self._state=0

    def add_subscribers(self,subscriber_obj):
        self._subscribers_list.append(subscriber_obj)
        print('Successfully Subscribed')

    def unsubscribe(self,subscriber_obj):
        self._subscribers_list.remove(subscriber_obj)
        print('Successfully removed subscription')

    def notify(self):
        for subscriber_obj in self._subscribers_list:
            print('Hello I am SMS Publisher. Sending an update.')
            subscriber_obj.subscriber_update(self._state)

    def list_subscribers(self):
        for subscriber_obj in self._subscribers_list:
            print(subscriber_obj)

    def business_logic_update(self):
        '''
        Simulates a state change and notifies subscribers
        '''
        self._state = randrange(0, 10)
        print('My state has changed. I am updating my subscribers')
        self.notify()

EmailPublisher = PublisherConcreteClass1()
SMSPublisher = PublisherConcreteClass2()
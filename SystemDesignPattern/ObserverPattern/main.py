'''
Contains code to implement the publisher-subscriber design pattern
'''

from publisher_code import EmailPublisher,SMSPublisher
from subscriber_code import SubscriberConcreteClass1,SubscriberConcreteClass2

if __name__ == '__main__':
    #Create subscriber objects
    subscriber1 = SubscriberConcreteClass1()
    subscriber2 = SubscriberConcreteClass1()

    #add the subscribers
    EmailPublisher.add_subscribers(subscriber1)
    EmailPublisher.add_subscribers(subscriber2)

    #list subscribers before removal
    EmailPublisher.list_subscribers()

    #notify the subscribers
    EmailPublisher.business_logic_update('Notify my subscribers')

    #remove subscriber2
    EmailPublisher.unsubscribe(subscriber2)

    #list subscribers
    EmailPublisher.list_subscribers()

    subscriber3 = SubscriberConcreteClass2()
    SMSPublisher.add_subscribers(subscriber3)
    SMSPublisher.business_logic_update()

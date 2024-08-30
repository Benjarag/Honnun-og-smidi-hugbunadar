from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def update(self, data: int) -> None:
        pass

class Publisher(ABC):
    @abstractmethod
    def subscribe(self, subscriber: Subscriber) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, subscriber: Subscriber) -> None:
        pass

    def notify_subscribers(self, data: int) -> None:
        pass

class ConcreteSubscriber1(Subscriber):
    def update(self, data: int) -> None:
        print(f"ConcreteSubscriber1: {data}")
    
class ConcreteSubscriber2(Subscriber):
    def update(self, data: int) -> None:
        print(f"ConcreteSubscriber2: {data}")


class ConcretePublisher(Publisher):
    def __init__(self):
        self.__subscribers = []
    
    def subscribe(self, subscriber: Subscriber) -> None:
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber) -> None:
        self.__subscribers.remove(subscriber)
            
    def notify_subscribers(self, data: int) -> None:
        for subscriber in self.__subscribers:
            subscriber.update(data)

    def some_business_logic(self, data: int) -> None:
        business_logic = data * data
        print(f"Publisher: I'm doing something important.")
        self.notify_subscribers(business_logic)
        print("\n")
    
if __name__ == "__main__":
    publisher = ConcretePublisher()

    subscriber1 = ConcreteSubscriber1()
    subscriber2 = ConcreteSubscriber2()

    publisher.subscribe(subscriber1)
    publisher.subscribe(subscriber2)

    publisher.some_business_logic(2)

    publisher.unsubscribe(subscriber2)

    publisher.some_business_logic(3)


    # publisher.some_business_logic(subscriber2)

    # publisher.some_business_logic(3)
    
    

from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def lay_egg(self):
        pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Penguin(Bird, Swimmable):
    def lay_egg(self):
        print('laying a penguin egg')

    def swim(self):
        print('swim swim')

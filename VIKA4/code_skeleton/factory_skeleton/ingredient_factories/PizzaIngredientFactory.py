from abc import ABC, abstractmethod


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def createDough():
        pass
    @abstractmethod
    def createSauce():
        pass
    @abstractmethod
    def createcheese():
        pass
    @abstractmethod
    def createVeggies():
        pass
    @abstractmethod
    def createPepperoni():
        pass
    @abstractmethod
    def createClam():
        pass


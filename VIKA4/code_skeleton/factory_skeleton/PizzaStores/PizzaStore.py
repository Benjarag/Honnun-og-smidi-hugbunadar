from abc import ABC, abstractmethod
from pizzas.PizzaType import PizzaType

class PizzaStore(ABC):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def order_pizza(self, pizza_type: PizzaType):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type: PizzaType):
        pass

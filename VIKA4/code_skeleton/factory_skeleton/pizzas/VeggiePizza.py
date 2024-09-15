

from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from pizzas.Pizza import Pizza


class VeggiePizza(Pizza):
    def __init__(self, ingredientFactory: PizzaIngredientFactory) -> None:
        self.__ingredientFactory = ingredientFactory

    def prepare(self):
        print(f"preparing: {self._name}")
        self._dough = self.__ingredientFactory.createDough()
        self._sauce = self.__ingredientFactory.createSauce()
        self._veggies = self.__ingredientFactory.createVeggies()
        self._cheese = self.__ingredientFactory.createcheese()

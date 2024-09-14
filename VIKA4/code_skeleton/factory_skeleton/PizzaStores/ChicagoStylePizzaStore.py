from PizzaStores.PizzaStore import PizzaStore
from ingredient_factories.ChicagoPizzaIngredientFactory import ChicagoPizzaIngredientFactory
from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from pizzas.CheesePizza import CheesePizza
from pizzas.PepperoniPizza import PepperoniPizza
from pizzas.ClamPizza import ClamPizza
from pizzas.VeggiePizza import VeggiePizza

from pizzas.PizzaType import PizzaType


class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        ingredientFactory = ChicagoPizzaIngredientFactory()
        pizza = None    
        if pizza_type == PizzaType.CHEESE:
            pizza = CheesePizza(ingredientFactory)
            pizza.set_name("Chicago Style Cheese Pizza")
        elif pizza_type == PizzaType.PEPPERONI:
            pizza = PepperoniPizza(ingredientFactory)
            pizza.set_name("Chicago Style Pepperoni Pizza")
        elif pizza_type == PizzaType.CLAM:
            pizza = ClamPizza(ingredientFactory)
            pizza.set_name("Chicago Style Clam Pizza")
        elif pizza_type == PizzaType.VEGGIE:
            pizza = VeggiePizza(ingredientFactory)
            pizza.set_name("Chicago Style Veggie Pizza")
        return pizza
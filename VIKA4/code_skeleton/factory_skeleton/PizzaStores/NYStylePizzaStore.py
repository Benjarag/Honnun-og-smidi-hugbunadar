from PizzaStores.PizzaStore import PizzaStore
from ingredient_factories.NYPizzaIngredientFactory import NYPizzaIngredientFactory
from pizzas.VeggiePizza import VeggiePizza
from pizzas.ClamPizza import ClamPizza
from pizzas.PepperoniPizza import PepperoniPizza
from pizzas.CheesePizza import CheesePizza
from pizzas.Pizza import Pizza
from pizzas.PizzaType import PizzaType

class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        ingredientFactory = NYPizzaIngredientFactory()
        pizza = None    
        if pizza_type == PizzaType.CHEESE:
            pizza = CheesePizza(ingredientFactory)
            pizza.set_name("New York Style Cheese Pizza")
        elif pizza_type == PizzaType.PEPPERONI:
            pizza = PepperoniPizza(ingredientFactory)
            pizza.set_name("New York Style Pepperoni Pizza")
        elif pizza_type == PizzaType.CLAM:
            pizza = ClamPizza(ingredientFactory)
            pizza.set_name("New York Style Clam Pizza")
        elif pizza_type == PizzaType.VEGGIE:
            pizza = VeggiePizza(ingredientFactory)
            pizza.set_name("New York Style Veggie Pizza")
        return pizza

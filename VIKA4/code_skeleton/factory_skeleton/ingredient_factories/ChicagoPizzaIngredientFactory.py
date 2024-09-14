from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from ingredients.cheese.Mozzarella import Mozzarella
from ingredients.clams.FrozenClams import FrozenClams
from ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from ingredients.sauce.PlumTomatoSauce import PlumTomatoSauce
from ingredients.veggies.Garlic import Garlic
from ingredients.veggies.Mushroom import Mushroom
from ingredients.veggies.Onion import Onion
from ingredients.veggies.RedPepper import RedPepper
from ingredients.dough.ThickCrustDough import ThickCrustDough


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThickCrustDough()
    def createSauce(self):
        return PlumTomatoSauce()
    def createcheese(self):
        return Mozzarella()
    def createVeggies(self):
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies
    def createPepperoni(self):
        return SlicedPepperoni()
    def createClam(self):
        return FrozenClams()


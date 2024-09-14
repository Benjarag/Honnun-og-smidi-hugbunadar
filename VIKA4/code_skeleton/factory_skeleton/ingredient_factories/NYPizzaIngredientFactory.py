from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from ingredients.cheese.ReggianoCheese import ReggianoCheese
from ingredients.clams.FreshClams import FreshClams
from ingredients.dough.ThinCrustDough import ThinCrustDough
from ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from ingredients.sauce.MarinaraSauce import MarinaraSauce
from ingredients.veggies.RedPepper import RedPepper
from ingredients.veggies.Mushroom import Mushroom
from ingredients.veggies.Onion import Onion
from ingredients.veggies.Garlic import Garlic



class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThinCrustDough()
    def createSauce(self):
        return MarinaraSauce()
    def createcheese(self):
        return ReggianoCheese()
    def createVeggies(self):
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies
    def createPepperoni(self):
        return SlicedPepperoni()
    def createClam(self):
        return FreshClams()

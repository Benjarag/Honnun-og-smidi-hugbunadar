

from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class BaseComponent(Component):
    def operation(self) -> str:
        return "BaseComponent"
    
class ComponentDecoratorA(Component):
    def __init__(self) -> None:
        self.__component 

# klára
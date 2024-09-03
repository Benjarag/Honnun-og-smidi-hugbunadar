from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class BaseComponent(Component):
    def operation(self) -> str:
        return "BaseComponent"
    

class ComponentDecoratorA(Component):
    def __init__(self, component: Component) -> None:
        self.__component = component

    def operation(self) -> str:
        return f"ComponentDecoratorA({self.__component.operation()})"

class ComponentDecoratorB(Component):
    def __init__(self, component: Component) -> None:
        self.__component = component

    def operation(self) -> str:
        return f"ComponentDecoratorB({self.__component.operation()})"


if __name__ == "__main__":
    simple = BaseComponent()
    print(simple.operation())

    simple = ComponentDecoratorA(simple)
    print(simple.operation())

    simple = ComponentDecoratorB(simple)
    print(simple.operation())

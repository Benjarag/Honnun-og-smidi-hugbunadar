from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def build(self, a: int, b: int) -> str:
        pass


class RoadStrategy(RouteStrategy):
    def build(self, a: int, b: int) -> str:
        return f"Road from {a} to {b}"

class SeaStrategy(RouteStrategy):
    def build(self, a: int, b: int) -> str:
        return f"Sea from {a} to {b}"

class Navigator:
    def __init__(self, route_strategy : RouteStrategy):
        self.__route_strategy = route_strategy
    
    def set_strategy(self, route_strategy: RouteStrategy):
        self.__route_strategy = route_strategy

    def build_route(self, a: int, b: int):
        print(self.__route_strategy.build(a, b))

if __name__ == "__main__":
    road_strategy = RoadStrategy()
    sea_strategy = SeaStrategy()

    navigator = Navigator(road_strategy)
    navigator.build_route(1, 2)

    navigator.set_strategy(sea_strategy)
    navigator.build_route(1, 2)
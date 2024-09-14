from abc import ABC, abstractmethod


class IRoundPeg(ABC):
    @abstractmethod
    def get_radius(self) -> int:
        pass

class RoundPeg(IRoundPeg):
    def __init__(self, radius: int) -> None:
        self.__radius = radius

    def get_radius(self) -> int:
        return self.__radius

class SquarePeg:
    def __init__(self, width: int) -> None:
        self.__width = width

    def get_width(self) -> int:
        return self.__width
    
class SquarePegAdapter(IRoundPeg):
    def __init__(self, peg: SquarePeg) -> None:
        self.__peg = peg
    
    def get_radius(self) -> int:
        return int(self.__peg.get_width() * 0.7071)

    
class RoundHole:
    def __init__(self, radius: int) -> None:
        self.__radius = radius
    
    def get_radius(self) -> int:
        return self.__radius

    def fits(self, peg: IRoundPeg) -> bool:
        return self.get_radius() >= peg.get_radius()
    

if __name__ == '__main__':
    hole = RoundHole(5)
    roundPeg = RoundPeg(5)

    print(hole.fits(roundPeg))

    squarePeg = SquarePeg(5)
    squarePegAdapter = SquarePegAdapter(squarePeg)

    print(hole.fits(squarePegAdapter))
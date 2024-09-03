from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def has_legs(self) -> bool:
        pass

    @abstractmethod
    def sit_on(self):
        pass


class VictorianChair(Chair):
    def has_legs(self) -> bool:
        return True
    
    def sit_on(self):
        print("Sitting on victorian chair")

class ModernChair(Chair):
    def has_legs(self) -> bool:
        return False
    
    def sit_on(self):
        print("Sitting on Modern chair")


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()
    
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()
    

if __name__ == "__main__":
    modern_factory = ModernFurnitureFactory()
    modern_chair = modern_factory.create_chair()
    print(modern_chair.has_legs())
    modern_chair.sit_on()

    victorian_factory = VictorianFurnitureFactory()
    victorian_chair = victorian_factory.create_chair()
    print(victorian_chair.has_legs())
    victorian_chair.sit_on()
    
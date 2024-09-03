from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def name(self):
        pass

class Logistics(ABC):
    def plan_deliver(self):
        transport = self.create_transport()
        print(f"Delivering using {transport.name()}")
    
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

class Truck(Transport):
    def name(self):
        return "Truck"

class Ship(Transport):
    def name(self):
        return "Ship"

class RoadLogistics(Logistics):
    def create_transport(self) -> str:
        return Truck()
    

class SeaLogistics(Logistics):
    def create_transport(self) -> str:
        return Ship()
    

if __name__ == "__main__":
    road_logistics = RoadLogistics()
    road_logistics.plan_deliver()

    sea_logistics = SeaLogistics()
    sea_logistics.plan_deliver()

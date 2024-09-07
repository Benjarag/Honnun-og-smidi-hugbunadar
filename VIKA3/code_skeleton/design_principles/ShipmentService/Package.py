
class Package:
    def __init__(self, id: int, shipment_type: str):
        self.id = id
        self.__shipment_type = shipment_type

    @property
    def shipment_type(self) -> str:
        return self.__shipment_type

class ShipmentType:
    SHIP = 'ship'
    PLANE = 'plane'
    CAR = 'car'
    CARRIER_PIGEON = 'carrier_pigeon'



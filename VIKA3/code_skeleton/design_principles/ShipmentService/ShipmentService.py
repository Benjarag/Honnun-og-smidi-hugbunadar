from Package import Package, ShipmentType
from Ship import Ship
from Plane import Plane
from Car import Car
from CarrierPigeon import CarrierPigeon

class ShipmentService:
    def __init__(self):
        self.Shipment_methods = {
            ShipmentType.SHIP: Ship(),
            ShipmentType.PLANE: Plane(),
            ShipmentType.CAR: Car(),
            ShipmentType.CARRIER_PIGEON: CarrierPigeon()
        }

    def ship(self, package: Package) -> None:
        shipment_method = self.Shipment_methods.get(package.shipment_type)
        if shipment_method:
            try:
                shipment_method.deliver_package(package)
            except Exception as e:
                print(f"Delivery error: {e}")
                
        else:
            print(f"Unknown Shipment type, {package.shipment_type}")
        
            
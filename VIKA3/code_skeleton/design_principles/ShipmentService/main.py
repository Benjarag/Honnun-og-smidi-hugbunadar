from Package import Package, ShipmentType
from ShipmentService import ShipmentService

def main():
    shipment_service = ShipmentService()
    
    # create Packages to deliver
    package1 = Package(id=1, shipment_type=ShipmentType.SHIP)
    package2 = Package(id=2, shipment_type=ShipmentType.PLANE)
    package3 = Package(id=3, shipment_type=ShipmentType.CAR)
    package4 = Package(id=4, shipment_type=ShipmentType.CARRIER_PIGEON)
    package5 = Package(id=5, shipment_type='race_car')  
    
    # testing package deliveries
    print("Testing package delivery:")
    shipment_service.ship(package1) 
    shipment_service.ship(package2) 
    shipment_service.ship(package3)  
    shipment_service.ship(package4) 
    shipment_service.ship(package5)  

if __name__ == "__main__":
    main()

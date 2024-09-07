from DeliveryStatus import DeliveryStatus
from Package import Package

class CarrierPigeon(DeliveryStatus):
    def prepare_for_delivery(self) -> None:
        print("The carrier pigeon is eating seeds")

    def deliver_package(self, package: Package) -> None:
        self.prepare_for_delivery
        print(f"The carrier pigeon is delivering package {package.id}")
from DeliveryStatus import DeliveryStatus
from Package import Package

class Plane(DeliveryStatus):
    def prepare_for_delivery(self) -> None:
        print("The plane is refueling with jet oil")

    def deliver_package(self, package: Package) -> None:
        self.prepare_for_delivery
        print(f"The plane is delivering package {package.id}")

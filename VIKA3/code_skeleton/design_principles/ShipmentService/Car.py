from DeliveryStatus import DeliveryStatus
from Package import Package

class Car(DeliveryStatus):
    def prepare_for_delivery(self) -> None:
        print("The car is refueling with gas")

    def deliver_package(self, package: Package) -> None:
        self.prepare_for_delivery
        print(f"The car is delivering package {package.id}")
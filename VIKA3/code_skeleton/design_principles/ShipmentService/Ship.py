from DeliveryStatus import DeliveryStatus
from Package import Package

class Ship(DeliveryStatus):
    def prepare_for_delivery(self) -> None:
        print("The ship is refueling with fuel oil")

    def deliver_package(self, package) -> None:
        self.prepare_for_delivery
        print(f"The ship is delivering package {package.id}")
from abc import ABC, abstractmethod


class DeliveryStatus(ABC):
    @abstractmethod
    def deliver_package(self, package) -> None:
        pass

    @abstractmethod
    def prepare_for_delivery(self) -> None:
        pass

from abc import ABC, abstractmethod

from Order import Order

# Interface for OrderSaver
class IOrderSaver(ABC):
    @abstractmethod
    def save_order(self, order: Order) -> None:
        pass

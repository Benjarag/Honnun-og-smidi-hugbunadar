from Order import Order
from IOrderSaver import IOrderSaver


class OrderSaver(IOrderSaver):
    def save_order(self, order: Order) -> None:
        # Saving logic should be implemented here
        pass
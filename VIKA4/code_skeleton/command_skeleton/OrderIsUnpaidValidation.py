from Validation import Validation
from models.Order import Order, OrderStatus

class OrderIsUnpaidValidation(Validation):
    def __init__(self, order: Order):
        self.order = order

    def validate(self) -> bool:
        return (self.order.status == OrderStatus.Unpaid)

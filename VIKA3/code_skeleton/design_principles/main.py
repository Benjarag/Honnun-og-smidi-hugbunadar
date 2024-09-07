# main.py, (AUKA vildi sjá hvort kóðinn virkaði svo ég lét bæta þessu við)

from Order import Order
from IOrderSaver import IOrderSaver
from IOrderCommitter import IOrderCommitter
from OrderSaver import OrderSaver
from OrderCommitter import OrderCommitter
from Connection import Connection
from OrderService import OrderService

# Example implementation for Connection
class Connection:
    def commit(self) -> None:
        print("Committing transaction...")

# Example implementation for OrderSaver
class OrderSaver(IOrderSaver):
    def save_order(self, order: Order) -> None:
        print("Saving order:", order)

# Example implementation for Order
class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id

    def __repr__(self):
        return f"Order({self.order_id})"

# Instantiate the concrete implementations
connection = Connection()
order_saver = OrderSaver()
order_committer = OrderCommitter(connection) 

# Instantiate OrderService with the dependencies
order_service = OrderService(order_saver, order_committer)

# Create a sample order
sample_order = Order(order_id=123)

# Run the submit_order method
order_service.submit_order(sample_order)

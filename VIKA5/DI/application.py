from injector import inject
from order_service import OrderService

class Application:
    @inject
    def __init__(self, order_service: OrderService) -> None:
        self.__order_service = order_service

    def run(self) -> None:
        username1 = 'john_doe'
        password1 = 'password123'

        order1 = 'Order #1'
        self.__order_service.create_order(username1, password1, order1)
        order2 = 'Order #2'
        self.__order_service.create_order(username1, password1, order2)
        password2 = 'john_doe'
        order3 = 'Order #3'
        self.__order_service.create_order(username1, password2, order3)
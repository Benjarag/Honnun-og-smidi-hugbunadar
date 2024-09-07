
from IOrderCommitter import IOrderCommitter
from Order import Order
from IOrderSaver import IOrderSaver


class OrderService:
    def __init__(self, order_saver: IOrderSaver, order_committer: IOrderCommitter):
        self.__order_committer = order_committer
        self.__order_saver = order_saver

    def submit_order(self, order: Order) -> None:
        self.__order_saver.save_order(order)
        self.__order_committer.commit() # Assuming commit is implemented
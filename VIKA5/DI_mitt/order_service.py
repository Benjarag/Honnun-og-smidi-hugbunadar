from injector import inject
from authentication_service import AuthenticationService
from logger import Logger
from order_repository import OrderRepository
from user_repository import UserRepository


class OrderService:
    @inject
    def __init__(self, user_repository: UserRepository, order_repository: OrderRepository, 
                 authentication_service: AuthenticationService, logger: Logger):
        self.user_repository = user_repository
        self.order_repository = order_repository
        self.authentication_service = authentication_service
        self.logger = logger

    def create_order(self, username: str, password: str, order_name: str) -> None:
        if self.__authentication_service.authenticate(username, password):
            self.__user_repository.add_user(username)
            self.__order_repository.add_order(order_name)
            self.__logger.log_info(
                f'Order {order_name} created for user {username}.')
        else:
            self.__logger.log_error(
                f'Failed to create order {order_name} for user {username}.')

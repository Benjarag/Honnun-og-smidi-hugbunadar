from logging import Logger
import sqlite3
from injector import Module, provider, singleton
from authentication_service import AuthenticationService
from order_repository import OrderRepository
from user_repository import UserRepository


class AppModule(Module):
    def __init__(self, environment: str, file_path: str) -> None:
        self.__environment = environment  # Fixed typo 'enviroment' to 'environment'
        self.__file_path = file_path

    @provider
    @singleton
    def provide_sqlite_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.__file_path)
    
    def configure(self, binder):
        binder.bind(UserRepository, to=UserRepository, scope=singleton)
        binder.bind(OrderRepository, to=OrderRepository, scope=singleton)
        binder.bind(AuthenticationService, to=AuthenticationService, scope=singleton)
        binder.bind(Logger, to=Logger, scope=singleton)
from logging import Logger
import sqlite3
from injector import Module, provider, singleton
from console_logger import ConsoleLogger
from db_logger import DbLogger
from authentication_service import AuthenticationService
from order_repository import OrderRepository
from user_repository import UserRepository


class AppModule(Module):
    def __init__(self, db_file: str, env: str) -> None:
        self.__db_file = db_file  
        self.__env = env

    @singleton
    @provider
    def provide_sqlite_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.__db_file)
    
    def configure(self, binder):
        if self.__env == "production":
            binder.bind(Logger, to=DbLogger, scope=singleton)
        else:
            binder.bind(Logger, to=ConsoleLogger, scope=singleton)

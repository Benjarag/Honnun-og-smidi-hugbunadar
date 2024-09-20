import sqlite3
from injector import Binder, Module, provider, singleton, noscope
from console_logger import ConsoleLogger
from db_logger import DbLogger
from logger import Logger


class AppModule(Module):
    def __init__(self, environment: str, file_path: str) -> None:
        self.__environment = environment
        self.__file_path = file_path

    @singleton
    @provider
    def provide_sqlite_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.__file_path)

    def configure(self, binder: Binder) -> None:
        binder.bind(
            Logger,
            to=(DbLogger if self.__environment == "production" else ConsoleLogger),
            scope=noscope,
        )

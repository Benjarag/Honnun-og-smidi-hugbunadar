import sqlite3

from injector import inject

from logger import Logger


class OrderRepository:
    @inject
    def __init__(self, connection: sqlite3.Connection, logger: Logger) -> None:
        self.__conn = connection
        self.__logger = logger

        with self.__conn:
            self.__conn.execute(
                "CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, order_name TEXT)"
            )

    def add_order(self, order_name: str) -> None:
        with self.__conn:
            self.__conn.execute(
                "INSERT INTO orders (order_name) VALUES (?)", (order_name,)
            )
            self.__logger.log_info(f"Order {order_name} added.")

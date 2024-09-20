import sqlite3

from injector import inject
from logger import Logger


class DbLogger(Logger):
    @inject
    def __init__(self, connection: sqlite3.Connection):
        self.__conn = connection

        with self.__conn:
            self.__conn.execute(
                "CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, type TEXT, message TEXT, exception TEXT)"
            )

    def log_info(self, message: str):
        with self.__conn:
            self.__conn.execute(
                "INSERT INTO logs (type, message) VALUES ('INFO', ?)", (message,)
            )

    def log_warning(self, message: str):
        with self.__conn:
            self.__conn.execute(
                "INSERT INTO logs (type, message) VALUES ('WARNING', ?)", (message,)
            )

    def log_error(self, message: str, exception: Exception = None):
        with self.__conn:
            self.__conn.execute(
                "INSERT INTO logs (type, message, exception) VALUES ('ERROR', ?, ?)",
                (message, str(exception)),
            )

    def close(self):
        self.__conn.close()

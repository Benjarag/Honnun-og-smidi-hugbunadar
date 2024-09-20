import sqlite3

from injector import inject

from logger import Logger


class UserRepository:
    @inject
    def __init__(self, connection: sqlite3.Connection, logger: Logger) -> None:
        self.__conn = connection
        self.__logger = logger

        with self.__conn:
            self.__conn.execute(
                "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)"
            )

    def add_user(self, username: str) -> None:
        with self.__conn:
            self.__conn.execute(
                "INSERT INTO users (username) VALUES (?)",
                (username,),
            )
            self.__logger.log_info(f"User {username} added.")

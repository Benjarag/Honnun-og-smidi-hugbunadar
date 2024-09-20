import sqlite3
from injector import inject
from logger import Logger

class UserRepository:
    @inject
    def __init__(self, connection: sqlite3.Connection, logger: Logger) -> None:
        self.__conn = connection
        self.__logger = logger

        # Create the users table if it doesn't exist
        with self.__conn:
            self.__conn.execute(
                "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)"
            )

    def add_user(self, username: str) -> None:
        """Adds a new user to the database."""
        try:
            with self.__conn:
                self.__conn.execute(
                    "INSERT INTO users (username) VALUES (?)", (username,)
                )
            self.__logger.log_info(f"User '{username}' added successfully.")
        except sqlite3.Error as e:
            self.__logger.log_error(f"Failed to add user '{username}': {e}")

    def get_user_by_id(self, user_id: int):
        """Retrieves a user by their ID."""
        try:
            cursor = self.__conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            user = cursor.fetchone()
            if user:
                self.__logger.log_info(f"User found with ID '{user_id}': {user}")
                return user
            else:
                self.__logger.log_info(f"No user found with ID '{user_id}'")
                return None
        except sqlite3.Error as e:
            self.__logger.log_error(f"Error retrieving user by ID '{user_id}': {e}")
            return None

    def get_user_by_username(self, username: str):
        """Retrieves a user by their username."""
        try:
            cursor = self.__conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
            if user:
                self.__logger.log_info(f"User found with username '{username}': {user}")
                return user
            else:
                self.__logger.log_info(f"No user found with username '{username}'")
                return None
        except sqlite3.Error as e:
            self.__logger.log_error(f"Error retrieving user by username '{username}': {e}")
            return None

    def delete_user(self, user_id: int) -> None:
        """Deletes a user by their ID."""
        try:
            with self.__conn:
                self.__conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
            self.__logger.log_info(f"User with ID '{user_id}' deleted successfully.")
        except sqlite3.Error as e:
            self.__logger.log_error(f"Failed to delete user with ID '{user_id}': {e}")

    def list_users(self):
        """Lists all users in the database."""
        try:
            cursor = self.__conn.cursor()
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            if users:
                self.__logger.log_info(f"Retrieved {len(users)} users.")
            else:
                self.__logger.log_info("No users found.")
            return users
        except sqlite3.Error as e:
            self.__logger.log_error(f"Error retrieving user list: {e}")
            return []

from Connection import Connection
from IOrderCommitter import IOrderCommitter

class OrderCommitter(IOrderCommitter):
    def __init__(self, connection: Connection):
        self.__connection = connection # creates some connection

    def commit(self) -> None:
        # commits order
        self.__connection.commit() # Assuming commit is implemented

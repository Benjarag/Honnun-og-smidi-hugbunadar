from abc import ABC, abstractmethod

# Interface for OrderCommiter
class IOrderCommitter(ABC):
    @abstractmethod
    def commit(self) -> None:
        pass
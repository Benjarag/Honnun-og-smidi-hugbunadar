from abc import ABC


class Chair(ABC):
    @abstractmethod
    def has_legs(self) -> bool:
        pass

    
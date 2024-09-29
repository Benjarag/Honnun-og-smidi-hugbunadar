from abc import ABC, abstractmethod
from typing import List
from users.user import User


class IUserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[User]:
        """Retrieve all users."""
        pass

    @abstractmethod
    def create_user(self, user: User) -> None:
        """Create a new user."""
        pass

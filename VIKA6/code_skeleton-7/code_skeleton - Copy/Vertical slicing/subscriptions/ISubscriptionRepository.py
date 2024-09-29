from abc import ABC, abstractmethod
from typing import List
from subscriptions.subscription import Subscription


class ISubscriptionRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Subscription]:
        """Retrieve all subscriptions."""
        pass

    @abstractmethod
    def create_subscription(self, subscription: Subscription) -> None:
        """Create a new subscription."""
        pass

from abc import ABC, abstractmethod
from typing import List
from core_onion.models.pricing import Pricing


class IPricingRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Pricing]:
        """Retrieve all pricing records."""
        pass

    @abstractmethod
    def create_pricing(self, pricing: Pricing) -> None:
        """Create a new pricing record."""
        pass

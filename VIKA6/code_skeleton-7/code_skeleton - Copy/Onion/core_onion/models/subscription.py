from dataclasses import dataclass
from datetime import date
from core_onion.models.user import User
from core_onion.models.pricing import Pricing


@dataclass
class Subscription:
    start_date: date
    end_date: date
    pricing_id: int
    user_id: int
    pricing: Pricing = None
    user: User = None
    id: int = None

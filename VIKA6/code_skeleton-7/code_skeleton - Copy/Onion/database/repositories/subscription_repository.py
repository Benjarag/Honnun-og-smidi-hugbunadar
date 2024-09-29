from contextlib import AbstractContextManager
from typing import Callable

from injector import inject
from sqlalchemy.orm import Session,  joinedload
from core_onion.interfaces.ISubscriptionRepository import ISubscriptionRepository
from core_onion.models.pricing import Pricing
from core_onion.models.subscription import Subscription
from core_onion.models.user import User


class SubscriptionRepository(ISubscriptionRepository):
    @inject
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.__session_factory = session_factory

    def get_all(self) -> list[Subscription]:
        with self.__session_factory() as session:
            return session.query(Subscription) \
                .options(joinedload(Subscription.pricing)) \
                .options(joinedload(Subscription.user)) \
                .all()

    def create_subscription(self, subscription: Subscription) -> None:
        with self.__session_factory() as session:
            subscription.user = session.query(User).get(subscription.user_id)
            subscription.pricing = session.query(
                Pricing).get(subscription.pricing_id)
            session.add(subscription)
            session.commit()
            session.refresh(subscription.user)
            session.refresh(subscription.pricing)

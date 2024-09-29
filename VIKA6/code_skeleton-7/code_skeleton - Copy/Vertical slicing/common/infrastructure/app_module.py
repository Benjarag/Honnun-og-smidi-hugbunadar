from contextlib import AbstractContextManager
from typing import List, Callable

from injector import Binder, Module, provider, singleton, multiprovider
from sqlalchemy.orm import Session



from movies.IMovieRepository import IMovieRepository
from pricings.IPricingRepository import IPricingRepository
from subscriptions.ISubscriptionRepository import ISubscriptionRepository
from users.IUserRepository import IUserRepository
from common.database.database import Database
from common.database.mappings.mapping import Mapping
from movies.movie_mapping import MovieMapping
from pricings.pricing_mapping import PricingMapping
from subscriptions.subscription_mapping import SubscriptionMapping
from users.user_mapping import UserMapping
from movies.movie_repository import MovieRepository
from pricings.pricing_repository import PricingRepository
from subscriptions.subscription_repository import SubscriptionRepository
from users.user_repository import UserRepository
from common.infrastructure.settings import Settings


class AppModule(Module):
    def __init__(self, settings: Settings):
        self.__settings = settings

    @provider
    @singleton
    def provide_settings(self) -> Settings:
        return self.__settings

    @multiprovider
    @singleton
    def provide_mappings(self) -> List[Mapping]:
        # noinspection PyTypeChecker
        return [
            MovieMapping(),
            PricingMapping(),
            SubscriptionMapping(),
            UserMapping()
        ]

    @provider
    @singleton
    def provide_session_factory(self, database: Database) -> Callable[..., AbstractContextManager[Session]]:
        return database.session
    
    def configure(self, binder: Binder) -> None:
        binder.bind(IMovieRepository, to=MovieRepository)
        binder.bind(IPricingRepository, to=PricingRepository)
        binder.bind(ISubscriptionRepository, to=SubscriptionRepository)
        binder.bind(IUserRepository, to=UserRepository)
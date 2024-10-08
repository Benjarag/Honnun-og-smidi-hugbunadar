from injector import inject

from core_onion.interfaces.ISubscriptionRepository import ISubscriptionRepository
from core_onion.models.subscription import Subscription
from core_onion.services.twilio_gateway_fake import TwilioGatewayFake


class SubscriptionService:
    @inject
    def __init__(self, repository: ISubscriptionRepository, sms_service: TwilioGatewayFake):
        self.__sms_service = sms_service
        self.__repository = repository

    def get_all(self) -> list[Subscription]:
        return self.__repository.get_all()

    def create_subscription(self, subscription: Subscription) -> None:
        self.__repository.create_subscription(subscription)
        self.__sms_service.send_sms(subscription.user.phone_number,
                                    "You have been subscribed!")

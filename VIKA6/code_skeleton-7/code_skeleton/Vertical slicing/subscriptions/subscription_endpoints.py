from fastapi import APIRouter, Depends, status

from common.infrastructure.get_service import get_service
from subscriptions.subscription_service import SubscriptionService
from subscriptions.create_subscription_dto import CreateSubscriptionDto

from subscriptions.subscription import Subscription

router = APIRouter(
    prefix='/subscriptions',
)


@router.get('/')
def get_users(subscription_service: SubscriptionService = Depends(get_service(SubscriptionService))):
    return subscription_service.get_all()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request: CreateSubscriptionDto, subscription_service: SubscriptionService = Depends(get_service(SubscriptionService))):
    subscription = Subscription(
        start_date=request.start_date,
        end_date=request.end_date,
        user_id=request.user_id,
        pricing_id=request.pricing_id
    )

    subscription_service.create_subscription(
        subscription
    )

    return subscription

from fastapi import APIRouter, Depends, status

from common.infrastructure.get_service import get_service
from pricings.pricing_service import PricingService
from pricings.create_pricing_dto import CreatePricingDto

from pricings.pricing import Pricing

router = APIRouter(
    prefix='/pricings',
)


@router.get('/')
def get_pricings(pricing_service: PricingService = Depends(get_service(PricingService))):
    return pricing_service.get_all()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_pricing(request: CreatePricingDto, pricing_service: PricingService = Depends(get_service(PricingService))):
    pricing = Pricing(
        name=request.name,
        price=request.price,
    )

    pricing_service.create_pricing(
        pricing
    )

    return pricing

from fastapi import FastAPI

from pricings import pricing_endpoints
from subscriptions import subscription_endpoints
from users import user_endpoints
from movies import movie_endpoints

def __get_endpoint_modules():
    return [user_endpoints, movie_endpoints, pricing_endpoints, subscription_endpoints]


def create_app() -> FastAPI:
    endpoint_modules = __get_endpoint_modules()
    app = FastAPI()
    for module in endpoint_modules:
        app.include_router(module.router)
    return app

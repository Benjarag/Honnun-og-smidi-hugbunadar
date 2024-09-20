
import sqlite3
from injector import Injector
from authentication_service import AuthenticationService
from order_service import OrderService
from user_repository import UserRepository
from order_repository import OrderRepository
from console_logger import ConsoleLogger
from db_logger import DbLogger
from app_module import AppModule
from application import Application


# new main

db_file = 'application.db'
env = "production"

injector = Injector(AppModule(env, db_file))
# injector = Injector(AppModule())


application = injector.get(Application)

application.run()


# # old main

db_file = 'application.db'
env = "production"

connection = sqlite3.connect(db_file)

if env == "production":
    logger = DbLogger(connection)
else:
    logger = ConsoleLogger()


order_repository = OrderRepository(connection, logger)
user_repository = UserRepository(connection, logger)
authorization_service = AuthenticationService()
order_service = OrderService(
    user_repository, order_repository, authorization_service, logger)
application = Application(order_service)

application.run()


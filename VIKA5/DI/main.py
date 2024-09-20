from injector import Injector
from app_module import AppModule
from application import Application

db_file = "application.db"
env = "development"

injector = Injector(AppModule(env, db_file))

application = injector.get(Application)

application.run()

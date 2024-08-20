from logger import Logger


class ConsoleLogger(Logger):
    def log_info(self, message: str):
        print("info: " + message)

    def log_error(self, message: str, exception: Exception):
        print("error: " + message + ", exception: " + str(exception))

    def log_warning(self, message: str):
        print("warning: " + message)
    


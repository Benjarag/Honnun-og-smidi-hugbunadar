from logger import Logger 


class ConsoleLogger(Logger):
    def log_info(self, message: str):
        print(f'[INFO]: {message}')

    def log_warning(self, message: str):
        print(f'[WARNING]: {message}')

    def log_error(self, message: str, exception: Exception = None):
        print(f'[ERROR]: {message}', end=' ')
        if exception:
            print(f'[EXCEPTION]: {exception}')
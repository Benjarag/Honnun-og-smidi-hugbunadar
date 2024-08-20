from logger import Logger
import os

class FileLogger(Logger):
    def __init__(self, file_path: str = './logging.log'):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w'):
                pass


    def log_info(self, message: str):
        with open(self.file_path, 'a') as logfile:
            logfile.write(f"info : {message} \n")       

    def log_warning(self, message: str):
        with open(self.file_path, 'a') as logfile:
            logfile.write(f"warning : {message} \n" )
     
    def log_error(self, message: str, exception: Exception):
        with open(self.file_path, 'a') as logfile:
            logfile.write(f"error : {message} , exception: {str(exception)}\n")


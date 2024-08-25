from abc import ABC, abstractmethod


class StringFactory(ABC):
    @abstractmethod
    def create_string(self):
        pass

class UppercaseStringFactory(StringFactory):
    def create_string(self):
        return "HELLO"

class LowercaseStringFactory(StringFactory):
    def create_string(self):
        return "hello"



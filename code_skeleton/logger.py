# 2.1 Logger interface (15 stig)
# 1. (Heildar stig: 12.5) Útfærði Logger interface, interface-ið skal geyma í skrá sem ber nafnið logger.py
# og skal það interface hafa allar þær aðgerðir sem teknar eru fram í myndinni að ofan.
# 2. (Heildar stig: 2.5) Reynið að initalize-a Logger interface-ið og takið fram þau villuskilaboð sem eiga
# sér stað (það sem er átt með initialize er einfaldlega að reyna að búa til tilvik af klasanum)


from abc import ABC, abstractmethod


class Logger(ABC):

    @abstractmethod
    def log_error(message: str, exception: Exception):
        pass
    
    @abstractmethod
    def log_info(message: str):
        pass

    @abstractmethod
    def log_warning(message: str):
        pass
from abc import ABC

from IWeatherData import IWeatherData
from Observable import Observable



class ObservableWeatherData(Observable, IWeatherData, ABC):
    def __init__(self):
        super().__init__() # This should implement everything exactlu like the WeatherData class
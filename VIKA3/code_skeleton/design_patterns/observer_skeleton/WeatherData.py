# from Observer import Observer
from typing import List
from Observable import Observable
from Observer import Observer
from WeatherDataMeasurements import WeatherDataMeasurements
from IWeatherData import IWeatherData

class WeatherData(IWeatherData, Observable):
    def __init__(self):
        # Initialize an empty list of observers and the measurements
        self.__observers: List[Observer] = []
        self.__measurements = WeatherDataMeasurements(0.0, 0.0, 0.0)


    def register_observer(self, observer: Observer) -> None:
        """
        Registers an observer to the list
        """
        if observer not in self.__observers:
            self.__observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        """
        Removes an observer from the list
        """
        try:
            self.__observers.remove(observer)
        except ValueError:
            print(f"Observer {observer} not found in the list")

    def notify_observers(self) -> None:
        """
        Notifies all observers of changes
        """
        for observer in self.__observers:
            observer.update(self)

    def set_measurements(self, measurements: WeatherDataMeasurements) -> None:
        """
        Sets new measurements and notifies observers of the changes
        """
        self.__measurements = measurements
        self.notify_observers()

    def get_measurements(self) -> WeatherDataMeasurements:
        """
        Returns the current measurements
        """
        return self.__measurements

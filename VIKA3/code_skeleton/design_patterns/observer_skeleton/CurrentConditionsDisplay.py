from Observer import Observer
from IWeatherData import IWeatherData
from WeatherDataMeasurements import WeatherDataMeasurements
from WeatherData import WeatherData
from DisplayElement import DisplayElement

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self):
        self.temperature = 0.0
        self.humidity = 0.0

    def update(self, observable: WeatherDataMeasurements) -> None:
        if isinstance(observable, IWeatherData):
            measurement = observable.get_measurements()
            self.temperature = measurement.temperature
            self.humidity = measurement.humidity
            self.display()
    
    def display(self):
        print(f"Current conditions: {self.temperature:.1f}F degrees and {self.humidity:.1f}% humidity")
        

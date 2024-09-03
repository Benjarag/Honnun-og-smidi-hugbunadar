from Observer import Observer
from WeatherDataMeasurements import WeatherDataMeasurements
from IWeatherData import IWeatherData




class WeatherData(Observer, IWeatherData):
    def __init__(self):
        self.observers = []
        self.measurements = self.get_measurements()
        self.temperature = self.measurements.temperature
        self.humidity = self.measurements.humidity
        self.pressure = self.measurements.pressure

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        i = self.observers.index(observer)
        if (i >= 0):
            self.observers.remove(i)

    def notify_observers(self):
        for observer in self.observers:
            observer = Observer.update(self.temperature, self.humidity, self.pressure)


    def set_measurements(measurements: WeatherDataMeasurements):
        pass

    def get_measurements(self):
        return WeatherDataMeasurements()
        


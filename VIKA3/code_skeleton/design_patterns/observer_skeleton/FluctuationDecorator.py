from ObservableWeatherData import ObservableWeatherData
from WeatherDataMeasurements import WeatherDataMeasurements

class FluctuationDecorator(ObservableWeatherData):
    def __init__(self, weather_data: ObservableWeatherData):
        super().__init__()
        self.__weather_data = weather_data
        self.__min_temp_change = 1.0 # change the minimum temp change here, if needed
        self.__measurements = WeatherDataMeasurements(0.0, 0.0, 0.0)

    def __is_temp_change(self, measurements: WeatherDataMeasurements) -> bool:
        temperature_change = abs(measurements.temperature - self.__measurements.temperature)
        return temperature_change >= self.__min_temp_change

    def register_observer(self, observer) -> None:
        self.__weather_data.register_observer(observer)

    def remove_observer(self, observer) -> None:
        self.__weather_data.remove_observer(observer)

    def notify_observers(self) -> None:
        self.__weather_data.notify_observers()

    def set_measurements(self, measurements: WeatherDataMeasurements) -> None:
        if self.__is_temp_change(measurements):
            self.__measurements = measurements
            self.__weather_data.set_measurements(measurements)

    def get_measurements(self) -> WeatherDataMeasurements:
        return self.__weather_data.get_measurements()

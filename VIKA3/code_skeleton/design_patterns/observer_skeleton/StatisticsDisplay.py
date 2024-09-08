from Observer import Observer
from IWeatherData import IWeatherData


class TemperatureCalculator:
    def __init__(self):
        self.max_temp = float('-inf')
        self.min_temp = float('inf')
        self.temp_sum = 0.0
        self.num_readings = 0

    def update_statistics(self, temperature: float) -> None:
        self.temp_sum += temperature
        self.num_readings += 1

        if temperature > self.max_temp:
            self.max_temp = temperature
        if temperature < self.min_temp:
            self.min_temp = temperature

    def get_avg_temp(self) -> float:
        if self.num_readings == 0:
            return 0.0
        return self.temp_sum / self.num_readings

    def get_max_temp(self) -> float:
        return self.max_temp

    def get_min_temp(self) -> float:
        return self.min_temp

class StatisticsDisplay(Observer):
    def __init__(self):
        self.temp_calculator = TemperatureCalculator()

    def update(self, observable: Observer) -> None:
        if isinstance(observable, IWeatherData):
            measurement = observable.get_measurements()
            temperature = measurement.temperature
            self.temp_calculator.update_statistics(temperature)
            self.display()

    def display(self) -> None:
        avg_temp = self.temp_calculator.get_avg_temp()
        max_temp = self.temp_calculator.get_max_temp()
        min_temp = self.temp_calculator.get_min_temp()
        print(f"Avg/Max/Min temperature = {avg_temp:.1f}/{max_temp:.1f}/{min_temp:.1f}")
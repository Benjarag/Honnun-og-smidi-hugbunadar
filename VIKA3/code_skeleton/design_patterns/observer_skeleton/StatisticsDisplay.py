from Observer import Observer
from IWeatherData import IWeatherData
from StatisticsCalculator import TemperatureCalculator

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
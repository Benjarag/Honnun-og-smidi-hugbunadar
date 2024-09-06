

from Observer import Observer
from IWeatherData import IWeatherData


class StatisticsDisplay:
    def __init__(self):
        self._statistics = {
            'max_temp': float('-inf'),
            'min_temp': float('inf'),
            'temp_sum': 0.0,
            'num_readings': 0
        }
    
    def update(self, observable: Observer) -> None:
        if isinstance(observable, IWeatherData):
            measurement = observable.get_measurements()
            self.temperature = measurement.temperature

            self._statistics['temp_sum'] += self.temperature
            self._statistics['num_readings'] += 1

            if self.temperature > self._statistics['max_temp']:
                self._statistics['max_temp'] = self.temperature
            if self.temperature < self._statistics['min_temp']:
                self._statistics['min_temp'] = self.temperature

            self.display()

    def display(self) -> None:
        if self._statistics['num_readings'] > 0:
            avg_temp = self._statistics['temp_sum'] / self._statistics['num_readings']
            print(f"Avg/Max/Min temperature = {avg_temp:.1f}/{self._statistics['max_temp']:.1f}/{self._statistics['min_temp']:.1f}")


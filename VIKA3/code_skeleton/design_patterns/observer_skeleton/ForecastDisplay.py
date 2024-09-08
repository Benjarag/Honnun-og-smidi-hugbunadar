from Observable import Observable
from IWeatherData import IWeatherData
from StatisticsCalculator import PressureCalculator


class ForecastDisplay:
    def __init__(self) -> None:
        self.pressure_calculator = PressureCalculator()
        self.new_pressure = 0.0
        self.forecast = ""

    def update(self, observable: Observable) -> None:
        if isinstance(observable, IWeatherData):
            measurement = observable.get_measurements()
            new_pressure = measurement.pressure

            self.forecast = self.pressure_calculator.get_forecast(new_pressure)
            self.pressure_calculator.update_pressure(new_pressure)
            self.display()

    def display(self) -> None:
        print(f"Forecast: {self.forecast}")

    

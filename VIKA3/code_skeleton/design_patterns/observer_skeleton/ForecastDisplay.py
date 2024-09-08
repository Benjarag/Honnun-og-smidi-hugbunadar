from Observable import Observable
from IWeatherData import IWeatherData

class PressureForecast:
    def __init__(self):
        self.previous_pressure = 0.0 # should of course be None but kept it like this because in the pdf it got improving weather before getting a previous pressure

    def get_forecast(self, new_pressure: float) -> str:
        if self.previous_pressure is not None:
            if new_pressure > self.previous_pressure:
                return "Improving weather on the way!"
            elif new_pressure < self.previous_pressure:
                return "Watch out for cooler, rainy weather"
            else:
                return "More of the same"
        else:
            return "No previous data to compare"

    def update_pressure(self, new_pressure: float) -> None:
        self.previous_pressure = new_pressure


class ForecastDisplay:
    def __init__(self) -> None:
        self.pressure_calculator = PressureForecast()
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

    

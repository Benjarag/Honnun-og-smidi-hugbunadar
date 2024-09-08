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

class PressureCalculator:
    def __init__(self):
        self.previous_pressure = 0.0

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

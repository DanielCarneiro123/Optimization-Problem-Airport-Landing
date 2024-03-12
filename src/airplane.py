class Airplane:
    def __init__(self, fuel_level, fuel_consumption_rate, expected_landing_time):
        self.arriving_fuel_level = fuel_level
        self.fuel_consumption_rate = fuel_consumption_rate
        self.expected_landing_time = expected_landing_time
        self.actual_landing_time = None
        self.safe = self.ensure_enough_fuel()

    def __str__(self):
        return f"Fuel level: {self.arriving_fuel_level}, Fuel consumption rate: {self.fuel_consumption_rate}, Expected landing time: {self.expected_landing_time}, Actual landing time: {self.actual_landing_time}, Safety: {self.safe}"

    def get_arriving_fuel_level(self):
        return self.arriving_fuel_level

    def get_fuel_consumption_rate(self):
        return self.fuel_consumption_rate

    def get_expected_landing_time(self):
        return self.expected_landing_time

    def get_actual_landing_time(self):
        return self.actual_landing_time

    def get_safe(self):
        return self.safe

    def is_gonna_crash_init(self):
        actual_fuel_needed = self.fuel_consumption_rate * self.expected_landing_time
        return self.arriving_fuel_level < actual_fuel_needed

    def is_gonna_crash(self):
        actual_fuel_needed = self.fuel_consumption_rate * self.actual_landing_time
        return self.arriving_fuel_level < actual_fuel_needed

    def ensure_enough_fuel(self):
        fuel_needed = self.fuel_consumption_rate * 60
        fuel_left = (self.arriving_fuel_level - self.fuel_consumption_rate * self.expected_landing_time)
        return fuel_left >= fuel_needed
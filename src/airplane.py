class Airplane:
    def __init__(self, fuel_level, fuel_consumption_rate, expected_landing_time):
        # Initialize attributes
        self.arriving_fuel_level = fuel_level  # Initial fuel level
        self.fuel_consumption_rate = fuel_consumption_rate  # Fuel consumption rate
        self.expected_landing_time = expected_landing_time  # Expected landing time
        self.actual_landing_time = None  # Actual landing time
        self.safe = self.ensure_enough_fuel()  # Check if enough fuel for landing

    def __str__(self):
        # String representation
        return f"Fuel: {self.arriving_fuel_level}, Consumption: {self.fuel_consumption_rate}, Expected Landing: {self.expected_landing_time}, Actual Landing: {self.actual_landing_time}, Safe: {self.safe}"

    def is_gonna_crash_init(self):
        # Check if going to crash based on initial conditions
        actual_fuel_needed = self.fuel_consumption_rate * self.expected_landing_time
        return self.arriving_fuel_level < actual_fuel_needed

    def is_gonna_crash(self):
        # Check if going to crash based on actual conditions
        actual_fuel_needed = self.fuel_consumption_rate * self.actual_landing_time
        return self.arriving_fuel_level < actual_fuel_needed

    def ensure_enough_fuel(self):
        # Ensure enough fuel for a safe landing
        fuel_needed = self.fuel_consumption_rate * 60  # Fuel needed for 1 hour of flight
        fuel_left = self.arriving_fuel_level - self.fuel_consumption_rate * self.expected_landing_time  # Fuel left after expected flight
        return fuel_left >= fuel_needed  # Return True if enough fuel left for an hour

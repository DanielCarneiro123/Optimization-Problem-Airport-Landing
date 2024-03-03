import random


class Airplane:
    def __init__(self):
        self.arriving_fuel_level = int(random.uniform(1000, 5000))  # Level of fuel for the plane
        self.fuel_consumption_rate = int(random.uniform(5, 20))  # Fuel consumption rate
        self.expected_landing_time = int(random.uniform(10, 120))  # Expected time to reach the destination

    def mutate_airplane(self, other_airplane):
        self.arriving_fuel_level = other_airplane.arriving_fuel_level
        self.fuel_consumption_rate = other_airplane.fuel_consumption_rate
        self.expected_landing_time = other_airplane.expected_

    def mutate_airplane_arriving_fuel_level(self, other_airplane):
        self.arriving_fuel_level = other_airplane.arriving_fuel_level

    def mutate_airplane_arriving_fuel_rate(self, other_airplane):
        self.fuel_consumption_rate = other_airplane.fuel_consumption_rate

    def mutate_airplane_arriving_time(self, other_airplane):
        self.expected_landing_time = other_airplane.expected_landing_time

    def __eq__(self, other):
        if not isinstance(other,Airplane):
            return NotImplemented
        return self.arriving_fuel_level == other.arriving_fuel_level and self.fuel_consumption_rate == other.fuel_consumption_rate and self.expected_landing_time == other.expected_landing_time

    def print_airplane(self):
        print("\n" + "=" * 30)
        print("    Airplane Details Menu")
        print("=" * 30 + "\n")
        print(" " * 15 + "Genes\n")
        print("1. Arriving Fuel Level: {} gallons".format(self.arriving_fuel_level))
        print("2. Fuel Consumption Rate: {} gallons per minute".format(self.fuel_consumption_rate))
        print("3. Expected Landing Time: {} minutes".format(self.expected_landing_time))
        print("\n" + "=" * 30)




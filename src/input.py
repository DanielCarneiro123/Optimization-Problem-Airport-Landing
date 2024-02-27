import random
import pandas as pd
class Airplane:
    def __init__(self):
        self.arriving_fuel_level = random.uniform(1000, 5000)
        self.fuel_consumption_rate = random.uniform(5, 20)
        self.expected_landing_time = random.uniform(10, 120)

def generate_airplane_stream(num_airplanes):
    airplane_stream = [Airplane() for _ in range(num_airplanes)]
    return airplane_stream
# Example
## Generate a stream of 50airplanes
airplane_stream = generate_airplane_stream(50)
## Display the generated airplane stream
df = pd.DataFrame([(i, airplane.arriving_fuel_level,airplane.fuel_consumption_rate, airplane.expected_landing_time) for i,airplane in enumerate(airplane_stream, start=1)], columns=["Airplane","Fuel", "Consumption Rate", "Expected Landing Time"])
print(df)
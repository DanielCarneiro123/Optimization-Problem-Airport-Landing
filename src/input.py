import random
import pandas as pd
import math

class Airplane:
    def __init__(self):
        self.arriving_fuel_level = random.uniform(1000, 5000)
        self.fuel_consumption_rate = random.uniform(5, 20)
        self.expected_landing_time = random.uniform(10, 120)
        self.secure = True

    def anneal(self, input):
        airport_problem = AirportAllocationProblem()  # Criando uma instância de AirportAllocationProblem
        current_state = airport_problem.generate_airplane_stream(input)  # Chamando o método generate_airplane_stream
        current_cost = self.evaluate(current_state)
        best_state = current_state
        best_cost = current_cost
        temperature = 1.0
        cooling_rate = 0.99
        while temperature > 0.1:
            self.simulate_time_passage()  # Simular o passar do tempo
            new_state = self.neighbor(current_state)
            new_cost = self.evaluate(new_state)
            if self.acceptance_probability(current_cost, new_cost, temperature) > random.random():
                current_state = new_state
                current_cost = new_cost
            if new_cost < best_cost:
                best_state = new_state
                best_cost = new_cost
            temperature *= cooling_rate
        return best_state, best_cost

    def ensure_enough_fuel(airplane):
        # Calculate fuel needed for one hour of flight
        fuel_needed = airplane.fuel_consumption_rate * 60
        # Ensure arriving fuel level is enough for one hour of flight
        if airplane.arriving_fuel_level < fuel_needed:
            airplane.secure = False
            print(f"Airplane needs to land due to low fuel level! Current fuel level: {airplane.arriving_fuel_level}, Expected landing time: {airplane.expected_landing_time} minutes")


class AirportAllocationProblem:
    def __init__(self, num_pistas, num_avioes, ocupacao_pista=3):
        self.num_pistas = num_pistas
        self.num_avioes = num_avioes
        self.ocupacao_pista = ocupacao_pista
        self.airplane_stream = [Airplane() for _ in range(num_avioes)]

    def generate_airplane_stream(self, num_airplanes):  # Modificado para ser um método de instância
        airplane_stream = [Airplane() for _ in range(num_airplanes)]
        return airplane_stream


## Generate a stream of 50 airplanes
airplane_stream = generate_airplane_stream(60)

## Check fuel levels and force landing if necessary
for airplane in airplane_stream:
    ensure_enough_fuel(airplane)

## Display the generated airplane stream
df = pd.DataFrame([(i, airplane.arriving_fuel_level, airplane.fuel_consumption_rate, airplane.expected_landing_time, airplane.secure) for i, airplane in enumerate(airplane_stream, start=1)], columns=["Airplane", "Fuel", "Consumption Rate", "Expected Landing Time", "Safe Landing"])
print(df)

import random
import pandas as pd
import math
import copy
import random
import itertools

class Airplane:
    def __init__(self, fuel_level, fuel_consumption_rate, expected_landing_time):
        self.arriving_fuel_level = fuel_level
        self.fuel_consumption_rate = fuel_consumption_rate
        self.expected_landing_time = expected_landing_time
        self.actual_landing_time = 0 
        self.priority = 0

    def __str__(self):
        return f"Fuel level: {self.arriving_fuel_level}, Fuel consumption rate: {self.fuel_consumption_rate}, Expected landing time: {self.expected_landing_time}, Actual landing time: {self.actual_landing_time}"
        

    def ensure_enough_fuel(self):
        # Calculate fuel needed for one hour of flight
        fuel_needed = self.fuel_consumption_rate * 60
        # Ensure arriving fuel level is enough for one hour of flight
        if self.arriving_fuel_level < fuel_needed:
            self.priority = 1000  # Prioritize safety if fuel is insufficient
        else:
            self.priority = 1  # Prioritize schedule if fuel is sufficient

class LandingStrip:
    def __init__(self):
        self.current_airplanes = []  # List of airplanes currently on the landing strip
        self.empty_time = 0  # Time when the landing strip will be empty

    def add_airplane(self, airplane):
        self.current_airplanes.append(airplane)

    def remove_airplane(self, airplane):
        self.current_airplanes.remove(airplane)

    def set_empty_time(self, time):
        self.empty_time = time

    def get_empty_time(self):
        return self.empty_time

    def is_empty(self):
        return len(self.current_airplanes) == 0

    def land_airplane(self, airplane, landing_strips):
        if airplane.expected_landing_time > self.empty_time:
            max_empty_time = max(landing_strip.get_empty_time() for landing_strip in landing_strips)
            actual_landing_time = max(airplane.expected_landing_time, max_empty_time - 3)
            self.empty_time = actual_landing_time + 3
            airplane.actual_landing_time = actual_landing_time
            self.add_airplane(airplane)
        else:
            max_empty_time = max(landing_strip.get_empty_time() for landing_strip in landing_strips)
            min_empty_time_strip = min(range(len(landing_strips)), key=lambda i: landing_strips[i].get_empty_time())
            min_empty_time = landing_strips[min_empty_time_strip].get_empty_time()
            actual_landing_time = max(max_empty_time - 3, max(airplane.expected_landing_time, min_empty_time))
            landing_strips[min_empty_time_strip].set_empty_time(actual_landing_time + 3)
            airplane.actual_landing_time = actual_landing_time
            landing_strips[min_empty_time_strip].add_airplane(airplane)


    

    


class SimulatedAnnealing:
    def __init__(self, initial_solution, temperature, cooling_rate, stopping_temperature):
        self.current_solution = initial_solution
        self.best_solution = initial_solution
        self.temperature = temperature
        self.cooling_rate = cooling_rate
        self.stopping_temperature = stopping_temperature

    def acceptance_probability(self, cost_difference):
        if cost_difference < 0:
            return 1
        return math.exp(-cost_difference / self.temperature)

    def generate_neighbor(solution):
        neighbors = []
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                neighbor = copy.deepcopy(solution)
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors

    def cost_function(solution):
        cost = 0
        for airplane in solution:
            delay = airplane.actual_landing_time - airplane.expected_landing_time
            if delay > 0 and airplane.priority == 1:
                cost += delay
            elif airplane.priority > 1:
                cost += airplane.priority  
            elif delay > 0 and airplane.priority > 1:
                cost += delay * airplane.priority
            else:
                cost += airplane.priority
        return cost

    def optimize(self):
        while self.temperature > self.stopping_temperature:
            neighbor_solution = self.generate_neighbor(self.current_solution)
            cost_current = cost_function(self.current_solution)
            cost_neighbor = cost_function(neighbor_solution)
            cost_difference = cost_neighbor - cost_current

            if cost_difference < 0 or random.random() < self.acceptance_probability(cost_difference):
                self.current_solution = neighbor_solution

            if cost_function(self.current_solution) < cost_function(self.best_solution):
                self.best_solution = self.current_solution

            self.temperature *= self.cooling_rate

        return self.best_solution

    

    '''def generateResults(airplanes):
        landing_strips = [LandingStrip() for _ in range(3)]
        landed_airplanes = set()


        # Simulate landing airplanes on strips
        for airplane in airplanes:
            for landing_strip in landing_strips:
                if airplane not in landed_airplanes:
                    landing_strip.land_airplane(airplane, landing_strips)
                    landed_airplanes.add(airplane)
                    break

        # Calculate the sum of differences between actual and expected landing times for the current solution
        sum_difference = sum(airplane.actual_landing_time - airplane.expected_landing_time for airplane in airplanes)
        return landing_strips, sum_difference'''
        


'''def print_airplanes_and_strips(landing_strips, airplanes):
        for airplane in airplanes:
            print(airplane)
            print("-----------------\n")
        for i, landing_strip in enumerate(landing_strips):
            print(f"Landing Strip {i}:")
            for airplane in landing_strip.current_airplanes:
                print(airplane)
            print()



def generate_neighbors(airplanes):
    neighbors = []
    for permutation in itertools.permutations(airplanes):
        neighbor = [copy.deepcopy(plane) for plane in permutation]
        neighbors.append(neighbor)
    return neighbors
'''

initial_solution = 60  # Defina sua solução inicial
temperature = 60  # Defina a temperatura inicial
cooling_rate = 5  # Defina a taxa de resfriamento
stopping_temperature = 1  # Defina a temperatura de parada

# Inicialize o Simulated Annealing
sa = SimulatedAnnealing(initial_solution, temperature, cooling_rate, stopping_temperature)

# Execute o Simulated Annealing para otimizar a solução
best_solution = sa.optimize()

# Avalie a melhor solução encontrada
best_cost = cost_function(best_solution)

'''# Print the best solution
print("BEST SOLUTION")
print_airplanes_and_strips(*best_solution)
print("Min_Sum_Difference:", min_sum_difference)'''

'''
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
print(df)'''

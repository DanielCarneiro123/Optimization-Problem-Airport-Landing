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

    def get_arriving_fuel_level(self):
        return self.arriving_fuel_level

    def get_fuel_consumption_rate(self):
        return self.fuel_consumption_rate

    def get_expected_landing_time(self):
        return self.expected_landing_time

    def get_actual_landing_time(self):
        return self.actual_landing_time

    def get_priority(self):
        return self.priority

    def __str__(self):
        return f"Fuel level: {self.arriving_fuel_level}, Fuel consumption rate: {self.fuel_consumption_rate}, Expected landing time: {self.expected_landing_time}, Actual landing time: {self.actual_landing_time}"
        

    def ensure_enough_fuel(self):
        fuel_needed = self.fuel_consumption_rate * 60
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

    def get_current_airplanes(self):
        return self.current_airplanes
    

    def land_airplane(self, airplane, landing_strips):
        if airplane.expected_landing_time >= self.empty_time:
            # Se o tempo de pouso esperado for após o tempo vazio atual, não há necessidade de esperar
            actual_landing_time = airplane.expected_landing_time
            self.empty_time = actual_landing_time + 3
            airplane.actual_landing_time = actual_landing_time
            airplane.ensure_enough_fuel()
            self.add_airplane(airplane)
        else:
            # Se o tempo de pouso esperado for antes do tempo vazio atual, ajuste-o de acordo
            max_empty_time = max(landing_strip.get_empty_time() for landing_strip in landing_strips)
            min_empty_time_strip = min(range(len(landing_strips)), key=lambda i: landing_strips[i].get_empty_time())
            min_empty_time = landing_strips[min_empty_time_strip].get_empty_time()
            actual_landing_time = max(max_empty_time - 3, max(airplane.expected_landing_time, min_empty_time))
            landing_strips[min_empty_time_strip].set_empty_time(actual_landing_time + 3)
            airplane.actual_landing_time = actual_landing_time
            airplane.ensure_enough_fuel()
            landing_strips[min_empty_time_strip].add_airplane(airplane)


def cost_function(solution):
    cost = 0
    for landing_strip in solution:
        for airplane in landing_strip:
            print(airplane.get_actual_landing_time())
            print(airplane.get_expected_landing_time())
            print(airplane.get_priority())
            delay = airplane.get_actual_landing_time() - airplane.get_expected_landing_time()
            if delay > 0 and airplane.get_priority() == 1:
                cost += delay
            elif airplane.get_priority() > 1:
                cost += airplane.get_priority()
            elif delay > 0 and airplane.get_priority() > 1:
                cost += delay * airplane.get_priority()
            else:
                cost += airplane.get_priority()
    return cost




def generate_initial_solution(airplanes, landing_strips):
    initial_solution = [[] for _ in range(len(landing_strips))]
    for airplane in airplanes:
        landing_strip_index = random.randint(0, len(landing_strips) - 1)
        initial_solution[landing_strip_index].append(airplane)
    return initial_solution




def generate_neighbors(airplanes):
    neighbors = []
    num_airplanes = len(airplanes)

    
    # Iterate through all possible pairs of airplanes
    for i in range(num_airplanes):
        for j in range(i + 1, num_airplanes):
                for k in range(i + 2, num_airplanes):
                    # Create a new neighbor by swapping the positions of two airplanes
                    neighbor = airplanes[:]
                    neighbor[i], neighbor[j], neighbor[k] = neighbor[j], neighbor[k], neighbor[i]
                    neighbors.append(neighbor)
    
    return neighbors


def simulated_annealing(airplanes, landing_strips, initial_temperature=1000, cooling_rate=0.00001, stopping_temperature=0.0001, max_iterations=1000):
    current_solution = generate_initial_solution(airplanes, landing_strips)
    for strip in current_solution:
            for airplane in strip:
                landing_strip = random.choice(landing_strips)
                landing_strip.land_airplane(airplane, landing_strips)
    generate_neighbors(current_solution)
    current_cost = cost_function(current_solution)
    best_solution = current_solution
    best_cost = current_cost
    temperature = initial_temperature
    iteration = 0
    
    while temperature > stopping_temperature and iteration < max_iterations:
        new_solution = copy.deepcopy(current_solution)  
        for strip in new_solution:
            for airplane in strip:
                landing_strip = random.choice(landing_strips)
                landing_strip.land_airplane(airplane, landing_strips)

        generate_neighbors(new_solution)
        new_cost = cost_function(new_solution)
        print(new_cost)
        delta_cost = new_cost - current_cost
        
        if delta_cost < 0 or math.exp(-delta_cost / temperature) > random.random():
            current_solution = new_solution
            current_cost = new_cost
            
            if new_cost < best_cost:
                print("here")
                best_solution = new_solution
                best_cost = new_cost
                
        temperature *= cooling_rate
        iteration += 1
        
    return best_solution, best_cost

# Uso do algoritmo
def main():
    airplanes = []
    for i in range(1, 41):
        fuel_level = random.randint(1000, 2000)  # Random fuel level between 1000 and 2000
        fuel_consumption_rate = random.randint(15, 25)  # Random fuel consumption rate between 15 and 25
        expected_landing_time = random.randint(0, 90)  # Random expected landing time between 0 and 90
        airplane = Airplane(fuel_level, fuel_consumption_rate, expected_landing_time)
        airplanes.append(airplane)
    landing_strip1 = LandingStrip()
    landing_strip2 = LandingStrip()
    landing_strip3 = LandingStrip()
    landing_strips = [landing_strip1, landing_strip2, landing_strip3]    
    best_solution, best_cost = simulated_annealing(airplanes, landing_strips)
    for strip in best_solution:
        print("Landing Strip:")
        for airplane in strip:
            print(airplane)
    
    print("Best cost:", best_cost)

if __name__ == "__main__":
    main()
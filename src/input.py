
'''



def get_neighbors(solution):
    # Generate neighboring solutions by swapping the landing times of airplanes on the landing strips
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = copy.deepcopy(solution)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors
def tabu_search(max_iterations, tabu_size, airplanes):
    current_solution = airplanes[:]
    best_solution = airplanes[:]
    tabu_list = []

    for _ in range(max_iterations):
        neighbors = get_neighbors(current_solution)
        best_neighbor = None
        best_neighbor_value = (float('inf'), float('-inf'), float('-inf'))  # Initialize with large values

        for neighbor in neighbors:
            if neighbor not in tabu_list:
                neighbor_value = evaluate_solution(neighbor)
                if (neighbor_value[2], neighbor_value[0]) < (best_neighbor_value[2], best_neighbor_value[0]):  # Compare based on expected landing time first, then risk of crashes
                    best_neighbor = neighbor
                    best_neighbor_value = neighbor_value

        if best_neighbor is None:
            break

        current_solution = best_neighbor
        if (evaluate_solution(current_solution)[2], evaluate_solution(current_solution)[0]) < (evaluate_solution(best_solution)[2], evaluate_solution(best_solution)[0]):  # Compare based on expected landing time first, then risk of crashes
            best_solution = current_solution

        tabu_list.append(best_neighbor)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    return best_solution



# Example usage
num_airplanes = 4
airplanes = generate_airplanes(num_airplanes)
best_solution = tabu_search(max_iterations=10, tabu_size=10, airplanes=airplanes)
print("Best solution found:")
for airplane in best_solution:
    print(airplane)
print("Evaluation:", evaluate_solution(best_solution))


import random


def objective_function(x):
    return x**2 + 3*x - 4


def initial_solution():
    return random.uniform(-10, 10)


def get_neighbors(solution):
    return [solution + random.uniform(-0.5, 0.5)]

# Evaluate the quality of a solution (lower value is better)
def evaluate(solution):
    return objective_function(solution)

def tabu_search(max_iterations, tabu_size):
    current_solution = initial_solution()
    best_solution = current_solution
    tabu_list = []

    for _ in range(max_iterations):
        neighbors = get_neighbors(current_solution)
        best_neighbor = None
        best_neighbor_value = float('inf')

        for neighbor in neighbors:
            if neighbor not in tabu_list:
                neighbor_value = evaluate(neighbor)
                if neighbor_value < best_neighbor_value:
                    best_neighbor = neighbor
                    best_neighbor_value = neighbor_value

        if best_neighbor is None:
            break

        current_solution = best_neighbor
        if evaluate(current_solution) < evaluate(best_solution):
            best_solution = current_solution

        tabu_list.append(best_neighbor)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    return best_solution

# Example usage
best_solution = tabu_search(max_iterations=100, tabu_size=10)
print("Best solution found:", best_solution)
print("Objective function value:", evaluate(best_solution))

'''

import copy
import random
import itertools

class Airplane:
    def __init__(self, fuel_level, fuel_consumption_rate, expected_landing_time):
        self.arriving_fuel_level = fuel_level
        self.fuel_consumption_rate = fuel_consumption_rate
        self.expected_landing_time = expected_landing_time
        self.actual_landing_time = None
        self.safe = self.ensure_enough_fuel()

    def __str__(self):
        return f"Fuel level: {self.arriving_fuel_level}, Fuel consumption rate: {self.fuel_consumption_rate}, Expected landing time: {self.expected_landing_time}, Actual landing time: {self.actual_landing_time}, Safety: {self.safe}"

    def ensure_enough_fuel(self):
        fuel_needed = self.fuel_consumption_rate * 60
        # Ensure arriving fuel level is enough for one hour of flight
        return self.arriving_fuel_level >= fuel_needed
    
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
    
    def count_unsafe_airplanes(self):
        return sum(1 for airplane in self.current_airplanes if not airplane.safe)

    def land_airplane(self, airplane, landing_strips):
        
        if airplane.expected_landing_time >= self.empty_time:
            # If the expected landing time is after the current empty time, no waiting is needed
            actual_landing_time = airplane.expected_landing_time
            self.empty_time = actual_landing_time + 3
            airplane.actual_landing_time = actual_landing_time
            self.add_airplane(airplane)
        else:
            # If the expected landing time is before the current empty time, adjust accordingly
            max_empty_time = max(landing_strip.get_empty_time() for landing_strip in landing_strips)
            min_empty_time_strip = min(range(len(landing_strips)), key=lambda i: landing_strips[i].get_empty_time())
            min_empty_time = landing_strips[min_empty_time_strip].get_empty_time()
            actual_landing_time = max(max_empty_time - 3, max(airplane.expected_landing_time, min_empty_time))
            landing_strips[min_empty_time_strip].set_empty_time(actual_landing_time + 3)
            airplane.actual_landing_time = actual_landing_time
            landing_strips[min_empty_time_strip].add_airplane(airplane)


    

    def generateResults(airplanes):
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
        
        return landing_strips, sum_difference

def find_best_solution(neighbors):
    min_difference = float('inf')
    best_solution = None
    unsafe_planes = 0
    
    while True:
        for neighbor_index, neighbor in enumerate(neighbors):
            
            landing_strips, sum_difference = LandingStrip.generateResults(neighbor)        
            
            
            # Check if the solution is consistent and update the best solution if applicable
            if sum_difference < min_difference and sum(plane.actual_landing_time != plane.expected_landing_time for strip in landing_strips for plane in strip.current_airplanes if not plane.safe) <= unsafe_planes:
                min_difference = sum_difference
                best_solution = (landing_strips, sum_difference)
        
        if best_solution:
            print("Best solution after evaluating all neighbors:")
            print_airplanes_and_strips(*best_solution)
            return best_solution
        else:
            print("No consistent solution found with", unsafe_planes, "unsafe planes not landing instantly")
            unsafe_planes += 1









def print_airplanes_and_strips(landing_strips, sum_difference):
    print("Sum of differences between actual and expected landing times:", sum_difference)
    for i, landing_strip in enumerate(landing_strips):
        print(f"Landing Strip {i}:")
        for airplane in landing_strip.current_airplanes:
            print(airplane)
        print()



def generate_neighbors(airplanes):
    neighbors = []
    for permutation in itertools.permutations(airplanes):
        neighbor = [copy.deepcopy(plane) for plane in permutation]
        for plane in neighbor:
            plane.actual_landing_time = 0
        neighbors.append(neighbor)
    return neighbors

# Generate airplanes

airplane1 = Airplane(1100, 20, 89)
airplane2 = Airplane(1100, 20, 89)
airplane3 = Airplane(1100, 20, 90)

airplane4 = Airplane(1100, 20, 89)
airplane5 = Airplane(1100, 20, 89)

# Store airplanes in a list
airplanes = [airplane1, airplane2, airplane3,airplane4,airplane5]

# Generate neighbors
neighbors = generate_neighbors(airplanes)



best_solution = find_best_solution(neighbors)

# Print the best solution
print("BEST SOLUTION")
print_airplanes_and_strips(*best_solution)



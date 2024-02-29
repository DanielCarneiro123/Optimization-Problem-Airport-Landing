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

import random

class Airplane:
    '''def __init__(self):
        self.arriving_fuel_level = random.uniform(1000, 5000)
        self.fuel_consumption_rate = random.uniform(5, 20)
        self.expected_landing_time = random.uniform(10, 120)
        self.actual_landing_time = None  # Initialize actual landing time as None'''
    def __init__(self, fuel_level, fuel_consumption_rate, expected_landing_time):
        self.arriving_fuel_level = fuel_level
        self.fuel_consumption_rate = fuel_consumption_rate
        self.expected_landing_time = expected_landing_time
        self.actual_landing_time = None 

    def __str__(self):
        return f"Fuel level: {self.arriving_fuel_level}, Fuel consumption rate: {self.fuel_consumption_rate}, Expected landing time: {self.expected_landing_time}, Actual landing time: {self.actual_landing_time}"

def generate_airplanes(num_airplanes):
    return [Airplane() for _ in range(num_airplanes)]

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

    def land_airplane(self, airplane):
        if airplane.expected_landing_time > self.empty_time:
            max_empty_time = max(landing_strip.get_empty_time() for landing_strip in landing_strips)
            print(max_empty_time)
            # Landing strip is empty or airplane can land before it becomes empty
            actual_landing_time = max(airplane.expected_landing_time, max_empty_time-3)
            self.empty_time = actual_landing_time + 3
            airplane.actual_landing_time = actual_landing_time
            self.add_airplane(airplane)
        else:
            # Find the landing strip with the lowest empty time
           
            max_empty_time = max(landing_strip.get_empty_time() for landing_strip in landing_strips)
            print(max_empty_time)
            min_empty_time_strip = min(range(len(landing_strips)), key=lambda i: landing_strips[i].get_empty_time())
            min_empty_time = landing_strips[min_empty_time_strip].get_empty_time()
            actual_landing_time = max(max_empty_time-3,max(airplane.expected_landing_time, min_empty_time))
            landing_strips[min_empty_time_strip].set_empty_time(actual_landing_time + 3)
            airplane.actual_landing_time = actual_landing_time
            landing_strips[min_empty_time_strip].add_airplane(airplane)

# Create landing strips
landing_strips = [LandingStrip() for _ in range(3)]

# Generate airplanes
 # airplanes = generate_airplanes(5)

airplane1 = Airplane(4500, 15, 90)
airplane2 = Airplane(3000, 10, 91)
airplane3 = Airplane(3500, 18, 92)
airplane4 = Airplane(4000, 12, 30)
airplane5 = Airplane(5000, 20, 30)

# Store airplanes in a list
airplanes = [airplane1, airplane2, airplane3, airplane4, airplane5]

# Set to track landed airplanes
landed_airplanes = set()

# Simulate landing airplanes on strips
for airplane in airplanes:
    for landing_strip in landing_strips:
        if airplane not in landed_airplanes:
            landing_strip.land_airplane(airplane)
            landed_airplanes.add(airplane)
            break



def print_airplanes_and_strips(landing_strips, airplanes):
    for airplane in airplanes:
        print(airplane)
        print("-----------------\n")
    for i, landing_strip in enumerate(landing_strips):
        print(f"Landing Strip {i}:")
        for airplane in landing_strip.current_airplanes:
            print(airplane)
        print()



def shuffle_landing_order(airplanes):
    shuffled_airplanes = airplanes[:]
    random.shuffle(shuffled_airplanes)
    return shuffled_airplanes


# Print airplanes and their landing strips for the initial solution
print("Initial Solution:")
print_airplanes_and_strips(landing_strips,airplanes)

# Calculate the sum of differences between actual and expected landing times for the initial solution
sum_difference = sum(airplane.actual_landing_time - airplane.expected_landing_time for airplane in airplanes)
print("Sum of differences between actual and expected landing times (Initial Solution):", sum_difference)
'''
# Generate and print neighboring solutions by shuffling the landing order
num_neighbors = 3
for i in range(num_neighbors):
    shuffled_airplanes = shuffle_landing_order(airplanes)
    for airplane in shuffled_airplanes:
        for landing_strip in landing_strips:
            if airplane not in landed_airplanes:
                landing_strip.land_airplane(airplane)
                landed_airplanes.add(airplane)
                break
    print(f"Neighbor {i+1}:")
    print_airplanes_and_strips(landing_strips, shuffled_airplanes)

    # Calculate the sum of differences between actual and expected landing times for the neighboring solution
    sum_difference = sum(airplane.actual_landing_time - airplane.expected_landing_time for airplane in shuffled_airplanes)
    print("Sum of differences between actual and expected landing times (Neighbor):", sum_difference)
    print()'''
import random
import copy
'''
class Airplane:
    def __init__(self):
        self.arriving_fuel_level = random.uniform(1000, 5000)
        self.fuel_consumption_rate = random.uniform(5, 20)
        self.expected_landing_time = random.uniform(10, 120)

    def __str__(self):
        return f"Fuel level: {self.arriving_fuel_level}, Fuel consumption rate: {self.fuel_consumption_rate}, Expected landing time: {self.expected_landing_time}"


def generate_airplanes(num_airplanes):
    return [Airplane() for _ in range(num_airplanes)]
    
def evaluate_solution(solution):
    # Evaluation function to calculate the risk of crashes, fuel efficiency, and adherence to landing times
    risk_of_crashes = calculate_risk_of_crashes(solution)
    fuel_efficiency = calculate_fuel_efficiency(solution)
    adherence_to_landing_times = calculate_adherence_to_landing_times(solution)

    # Assuming we want to minimize risk, maximize fuel efficiency, and maximize adherence to landing times
    return risk_of_crashes, -fuel_efficiency, -adherence_to_landing_times

def calculate_risk_of_crashes(solution):
    risk_score = 0
    for i, airplane in enumerate(solution):
        remaining_fuel = airplane.arriving_fuel_level - (airplane.fuel_consumption_rate * (i+1))  # Fuel consumed based on position in landing queue
        if remaining_fuel < 60:  # Assuming 60 minutes (1 hour) as the safety threshold
            risk_score += 1
        if i > 0:  # Check if landing strip is occupied by another airplane
            previous_airplane = solution[i-1]
            if previous_airplane.expected_landing_time + 3 >= airplane.expected_landing_time:
                risk_score += 1  # Increase risk if landing strip is occupied
    return risk_score



def calculate_fuel_efficiency(solution):
    # Calculate fuel efficiency based on the remaining fuel levels of airplanes after landing
    total_fuel_consumed = sum(airplane.fuel_consumption_rate for airplane in solution)
    return total_fuel_consumed


def calculate_adherence_to_landing_times(solution):
    # Calculate adherence to landing times by comparing actual landing times to expected landing times
    adherence_score = sum(abs(airplane.expected_landing_time - actual_landing_time.expected_landing_time) for airplane, actual_landing_time in zip(solution, sorted(solution, key=lambda x: x.expected_landing_time)))
    return adherence_score


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

'''

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
